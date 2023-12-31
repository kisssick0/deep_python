import unittest
from unittest import mock

from predict1 import SomeModel
from predict1 import predict_message_mood


class TestPredict(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_simple(self):
        self.assertEqual(type(predict_message_mood("AAAA", self.model)), type("норм"))
        self.assertEqual(type(0.1), type(self.model.predict("VNFV")))

    def test_call_some_model_predict_with_message(self):
        msg = "hello"
        with mock.patch("predict1.SomeModel.predict") as mock_sm_predict:
            mock_sm_predict.return_value = 0.5
            mock_sm_predict(msg)
            mock_sm_predict.assert_called_with(msg)

    def test_call(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0.5
            predict_message_mood("AAAA", self.model)
            mock_sm.assert_called_once_with("AAAA")

    def test_get_predict_with_default_thresholds(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0.0

            self.assertEqual(0.0, mock_sm('AAAA'))
            self.assertEqual("неуд", predict_message_mood("AAAA", self.model))
            self.assertEqual(0.0, mock_sm('AAAA'))

            mock_sm.return_value = 0.55

            self.assertEqual(0.55, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model))
            self.assertEqual(0.55, mock_sm('AAAA'))

            mock_sm.return_value = 0.955

            self.assertEqual(0.955, mock_sm('AAAA'))
            self.assertEqual("отл", predict_message_mood("AAAA", self.model))
            self.assertEqual(0.955, mock_sm('AAAA'))

    def test_get_corner_predict(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0.3

            self.assertEqual(0.3, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model))
            self.assertEqual(0.3, mock_sm('AAAA'))

            mock_sm.return_value = 0.8

            self.assertEqual(0.8, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model))
            self.assertEqual(0.8, mock_sm('AAAA'))

    def test_get_predict_with_new_thresholds(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0.0001

            self.assertEqual(0.0001, mock_sm('AAAA'))
            self.assertEqual("неуд", predict_message_mood("AAAA", self.model, 0.0002, 0.0003))
            self.assertEqual(0.0001, mock_sm('AAAA'))

            mock_sm.return_value = 0.999

            self.assertEqual(0.999, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model, 0.9, 0.9999))
            self.assertEqual(0.999, mock_sm('AAAA'))

            mock_sm.return_value = 0.999

            self.assertEqual(0.999, mock_sm('AAAA'))
            self.assertEqual("отл", predict_message_mood("AAAA", self.model, 0.5, 0.99))
            self.assertEqual(0.999, mock_sm('AAAA'))

    def test_get_predict_with_corner_thresholds(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0

            self.assertEqual(0.0, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model, 0.0, 1.0))
            self.assertEqual(0.0, mock_sm('AAAA'))

            mock_sm.return_value = 1.0

            self.assertEqual(1.0, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model, 0.0, 1.0))
            self.assertEqual(1.0, mock_sm('AAAA'))

            mock_sm.return_value = 0.5

            self.assertEqual(0.5, mock_sm('AAAA'))
            self.assertEqual("норм", predict_message_mood("AAAA", self.model, 0.0, 1.0))
            self.assertEqual(0.5, mock_sm('AAAA'))

    def test_type_error_thresholds(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0.5

            self.assertEqual(0.5, mock_sm('AAAA'))
            with self.assertRaises(TypeError):
                predict_message_mood("AAAA", self.model, 'a', 0.5)
            self.assertEqual(0.5, mock_sm('AAAA'))

            self.assertEqual(0.5, mock_sm('AAAA'))
            with self.assertRaises(TypeError):
                predict_message_mood("AAAA", self.model, 0.5, 'a')
            self.assertEqual(0.5, mock_sm('AAAA'))

    def test_value_error_thresholds(self):
        with mock.patch("predict1.SomeModel.predict") as mock_sm:
            mock_sm.return_value = 0.5

            self.assertEqual(0.5, mock_sm('AAAA'))
            with self.assertRaises(ValueError):
                predict_message_mood("AAAA", self.model, 0.8, 0.5)
            self.assertEqual(0.5, mock_sm('AAAA'))


if __name__ == '__main__':
    unittest.main()
