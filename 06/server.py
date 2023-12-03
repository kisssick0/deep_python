import socket
import sys
import time
import threading
import queue
import argparse
from url_handler import url_handler


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--workers_count', type=int, required=True, nargs=1)
    parser.add_argument('-k', '--top_count', type=int, required=True, nargs=1)

    args = parser.parse_args()
    return args.workers_count[0], args.top_count[0]


class Server:
    def __init__(self, worker_num=10, top_k=5, handler_func=url_handler, handler_print=print):
        self.serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.serve_socket.bind(('', 53210))
        self.serve_socket.listen()
        self.top_k = top_k
        self.url_queue = queue.Queue()
        self.worker_num = worker_num
        self.url_handled = 0
        self.handler_func = handler_func
        self.handler_print = handler_print
        self.lock = threading.Lock()

    def run_server(self):
        threads = [threading.Thread(target=self.handle_request, args=[i], daemon=True)
                   for i in range(self.worker_num)]
        for thread in threads:
            thread.start()
        while True:
            client_sock, _ = self.serve_socket.accept()
            if not client_sock:
                self.url_queue.put(('end', None))
                break
            data = client_sock.recv(1024)
            if not data:
                self.url_queue.put(('end', None))
                break
            self.url_queue.put((data.decode('utf-8'), client_sock))
        for thread in threads:
            thread.join()

    def handle_request(self, thread_id):
        while True:
            data, client_sock = self.url_queue.get()
            if data == 'end':
                self.url_queue.put(('end', None))
                break
            try:
                data_handled = self.handler_func(data, self.top_k)
                client_sock.sendall(bytes(data_handled, encoding='utf-8'))
                self.handler_print(f'handled {self.url_handled} urls last by {thread_id}')
                client_sock.close()
                self.lock.acquire()
                self.url_handled += 1
                self.lock.release()
            except Exception as e:
                print(f'url {data} t_id{thread_id} error occured: {e}')
                continue


if __name__ == '__main__':
    workers_count, top_k_words = parse_arguments()

    server = Server(worker_num=workers_count, top_k=top_k_words)
    start = time.time()
    server.run_server()
    end = time.time()
    print(f'Time passed for {sys.argv[2]} workers: {end-start}')
