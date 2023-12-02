import socket
import sys
import time
import threading
import queue


def print_data(data, thread_id):
    print(data.decode(), f'thread:{thread_id}')


def make_socket_func() -> socket:
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)


class Client:
    def __init__(self, urls, thread_count=10, data_handler=print_data, make_socket=make_socket_func):
        self.urls = urls
        self.thread_count = thread_count
        self.url_queue = queue.Queue()
        self.threads = [
            threading.Thread(target=self.send_urls, args=[i], daemon=True)
            for i in range(self.thread_count)]
        self.data_handler = data_handler
        self.make_socket = make_socket
        for thread in self.threads:
            thread.start()

    def put_data(self):
        for url in self.urls:
            self.url_queue.put(url[0:len(url)-1])
        self.url_queue.put('end')
        for thread in self.threads:
            thread.join()

    def send_urls(self, thread_id=None):
        while True:
            url = self.url_queue.get()
            if url == 'end':
                self.url_queue.put('end')
                break
            try:
                client_sock = self.make_socket()
                client_sock.connect(('127.0.0.1', 53210))
                client_sock.sendall(url.encode('utf-8'))
                data = client_sock.recv(1024)
                self.data_handler(data, thread_id)
                client_sock.close()
            except Exception as e:
                print(f'url {url} t_id{thread_id} error occured: {e}')
                continue


if __name__ == '__main__':
    with open(sys.argv[2], "r") as file_:
        client = Client(urls=file_, thread_count=int(sys.argv[1]))
        start = time.time()
        client.put_data()
        end = time.time()
        print(f'Time passed for {sys.argv[1]} threads: {end-start}')
