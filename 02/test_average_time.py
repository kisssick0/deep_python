import unittest
from unittest.mock import patch
import time
from io import StringIO

import average_time


class TestParse(unittest.TestCase):
    @patch("average_time.koo")
    def test_twenty_calls_ten_mean(self, koo_mock):
        sleep_time = 0.1
        koo_mock.side_effect = lambda x: time.sleep(sleep_time)
        koo_mock.__name__ = 'koo'
        mean_koo = average_time.mean(10)(koo_mock)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(20):
                mean_koo(1)
                self.assertEqual(fake_out.getvalue()[:3], str(sleep_time))
                koo_mock.assert_called_with(1)

        self.assertTrue(koo_mock.called)
        self.assertEqual(koo_mock.call_count, 20)

    @patch("average_time.koo")
    def test_five_calls_five_mean(self, koo_mock):
        sleep_time = 0.1
        koo_mock.side_effect = lambda x: time.sleep(sleep_time)
        koo_mock.__name__ = 'koo'
        mean_koo = average_time.mean(5)(koo_mock)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(5):
                mean_koo(1)
                self.assertEqual(fake_out.getvalue()[:3], str(sleep_time))
                koo_mock.assert_called_with(1)

        self.assertTrue(koo_mock.called)
        self.assertEqual(koo_mock.call_count, 5)

    @patch("average_time.koo")
    def test_ten_calls_five_mean(self, koo_mock):
        sleep_time = 0.3
        koo_mock.side_effect = lambda x: time.sleep(sleep_time)
        koo_mock.__name__ = 'koo'
        mean_koo = average_time.mean(5)(koo_mock)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(10):
                mean_koo(1)
                self.assertEqual(fake_out.getvalue()[:3], str(sleep_time))
                koo_mock.assert_called_with(1)

        self.assertTrue(koo_mock.called)
        self.assertEqual(koo_mock.call_count, 10)

    @patch("average_time.koo")
    def test_five_calls_ten_mean(self, koo_mock):
        sleep_time = 0.5
        koo_mock.side_effect = lambda x: time.sleep(sleep_time)
        koo_mock.__name__ = 'koo'
        mean_koo = average_time.mean(10)(koo_mock)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(5):
                mean_koo(1)
                self.assertEqual(fake_out.getvalue()[:3], str(sleep_time))
                koo_mock.assert_called_with(1)

        self.assertTrue(koo_mock.called)
        self.assertEqual(koo_mock.call_count, 5)

    @patch("average_time.koo")
    def test_one_call_one_mean(self, koo_mock):
        sleep_time = 0.5
        koo_mock.side_effect = lambda x: time.sleep(sleep_time)
        koo_mock.__name__ = 'koo'
        mean_koo = average_time.mean(1)(koo_mock)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            mean_koo(1)
            self.assertEqual(fake_out.getvalue()[:3], str(sleep_time))
            koo_mock.assert_called_with(1)

        self.assertTrue(koo_mock.called)
        self.assertEqual(koo_mock.call_count, 1)

    @patch("average_time.koo")
    @patch("average_time.boo")
    def test_two_functions(self, koo_mock, boo_mock):
        koo_mock.__name__ = 'koo'
        koo_mock.side_effect = lambda x: time.sleep(0.1)
        boo_mock.__name__ = 'boo'
        boo_mock.side_effect = lambda x: time.sleep(0.2)

        mean_koo = average_time.mean(10)(koo_mock)
        mean_boo = average_time.mean(5)(boo_mock)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(4):
                mean_koo(1)
                self.assertEqual(fake_out.getvalue()[:3], str('0.1'))
                koo_mock.assert_called_with(1)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(4):
                mean_boo(1)
                self.assertEqual(fake_out.getvalue()[:3], str('0.2'))
                boo_mock.assert_called_with(1)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(6):
                mean_koo(1)
                self.assertEqual(fake_out.getvalue()[:3], str('0.1'))
                koo_mock.assert_called_with(1)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            for _ in range(6):
                mean_boo(1)
                self.assertEqual(fake_out.getvalue()[:3], str('0.2'))
                boo_mock.assert_called_with(1)

        self.assertTrue(koo_mock.called)
        self.assertEqual(koo_mock.call_count, 10)

        self.assertTrue(boo_mock.called)
        self.assertEqual(boo_mock.call_count, 10)

    @patch("average_time.koo")
    def test_type_error(self, koo_mock):
        koo_mock.side_effect = lambda x: time.sleep(0.5)
        koo_mock.__name__ = 'koo'

        with self.assertRaises(TypeError):
            average_time.mean('ah')(koo_mock)(1)

        self.assertFalse(koo_mock.called)

    @patch("average_time.koo")
    def test_zero_division_error(self, koo_mock):
        koo_mock.side_effect = lambda x: time.sleep(0.5)
        koo_mock.__name__ = 'koo'

        with self.assertRaises(ZeroDivisionError):
            average_time.mean(0)(koo_mock)(1)

        self.assertFalse(koo_mock.called)

    @patch("average_time.koo")
    def test_negative_number_error(self, koo_mock):
        koo_mock.side_effect = lambda x: time.sleep(0.5)
        koo_mock.__name__ = 'koo'

        with self.assertRaises(ValueError):
            average_time.mean(-1)(koo_mock)(1)

        self.assertFalse(koo_mock.called)


if __name__ == '__main__':
    unittest.main()
