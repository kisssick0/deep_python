import unittest
import io
from unittest import mock
import server
import client


class TestServer(unittest.TestCase):
    @mock.patch('socket.socket')
    def test_accept(self, serv_mock: mock.Mock):
        k = 2
        serv_mock.return_value = serv_mock

        client_mock = mock.Mock()
        client_mock.recv.side_effect = [b'https://en.wikipedia.org/wiki/Dino_Time', b'https://en.wikipedia.org/wiki/Dino_Time']
        serv_mock.accept.side_effect = [(client_mock, None), (client_mock, None), (None, None)]
        handler_func_mock = mock.Mock()
        handler_func_mock.return_value = 'foo'
        handler_print_mock = mock.Mock()

        server_ = server.Server(top_k=k, handler_func=handler_func_mock, handler_print=handler_print_mock)
        server_.run_server()
        self.assertEqual(3, serv_mock.accept.call_count)
        self.assertEqual(2, client_mock.recv.call_count)
        self.assertEqual(2, handler_func_mock.call_count)
        self.assertEqual(2, server_.handler_print.call_count)
        self.assertEqual(2, server_.url_handled)

    @mock.patch("socket.socket")
    @mock.patch("threading.Thread")
    def test_thread(self, thread_mock: mock.Mock, sock_mock: mock.Mock):
        thread_mock.return_value = thread_mock
        sock_mock.return_value = sock_mock
        sock_mock.accept.side_effect = [(None, None)]
        worker_num = 5

        server_ = server.Server(worker_num=worker_num)
        server_.run_server()
        self.assertEqual(worker_num, thread_mock.call_count)


class TestClient(unittest.TestCase):
    @mock.patch('socket.socket')
    def test_sender(self, mock_sock: mock.Mock):
        resp = io.StringIO()
        def mock_print(data, thread_id): print(data.decode(), file=resp)
        urls = ['https://en.wikipedia.org/wiki/Dino_Time']*2

        client_ = client.Client(urls=urls)
        client_.data_handler = mock_print

        mock_sock.return_value = mock_sock
        mock_sock.recv.side_effect = [
            'foo'.encode(encoding="utf-8"),
            "test".encode("utf-8")]

        client_.put_data()
        str_resp = resp.getvalue()
        self.assertEqual(str_resp, 'foo\ntest\n')
        self.assertEqual(mock_sock.call_count, 2)
        mock_sock.recv.assert_called_with(1024)
        self.assertEqual(mock_sock.close.call_count, 2)
        self.assertEqual(client_.url_queue.qsize(), 1)
        self.assertEqual(client_.url_queue.get(), 'end')

    @mock.patch('threading.Thread')
    def test_thread(self, thread_mock: mock.Mock):
        thread_mock.return_value = thread_mock

        thread_count = 5
        client_ = client.Client(urls=['end'], thread_count=thread_count)
        self.assertEqual(thread_count, thread_mock.call_count)
        self.assertEqual(thread_count, thread_mock.start.call_count)
        self.assertEqual(0, thread_mock.join.call_count)
        client_.put_data()
        self.assertEqual(thread_count, thread_mock.join.call_count)
