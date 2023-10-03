import unittest
from unittest.mock import patch
import parse


class TestParse(unittest.TestCase):
    def setUp(self):
        self.json_str = '{"key1": "small cat run", "Key1": "Big Cat", "key2": "smaLL dog", "key3": "big dog",' \
               '"key4": "many cats", "key5": "MANY dogs"}'

    @patch("parse.callback")
    def test_type_error(self, callback_mock):
        json_str = 5
        self.assertRaises(TypeError, parse.parse_json(json_str, ['key5'], ['dogs'], callback_mock), self.json_str)
        self.assertFalse(callback_mock.called)

    @patch("parse.callback")
    def test_required_fields_is_none(self, callback_mock):
        self.assertIsNone(parse.parse_json(self.json_str, callback_mock, keywords=['dogs']))
        self.assertFalse(callback_mock.called)

    @patch("parse.callback")
    def test_keywords_is_none(self, callback_mock):
        self.assertIsNone(parse.parse_json(self.json_str, ['key1'], None, callback_mock))
        self.assertFalse(callback_mock.called)

    @patch("parse.callback")
    def test_one_field_one_word(self, callback_mock):
        parse.parse_json(self.json_str, ['key5'], ['dogs'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)

    @patch("parse.callback")
    def test_one_field_two_words(self, callback_mock):
        parse.parse_json(self.json_str, ['key3'], ['big', 'dog'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)

    @patch("parse.callback")
    def test_two_fields_one_word(self, callback_mock):
        parse.parse_json(self.json_str, ['key2', 'key3'], ['dog'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)

    @patch("parse.callback")
    def test_keywords_register(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'Key1'], ['cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)

    @patch("parse.callback")
    def test_substring(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'key4'], ['cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)

    @patch("parse.callback")
    def test_required_fields_register(self, callback_mock):
        parse.parse_json(self.json_str, ['key1'], ['cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)

    @patch("parse.callback")
    def test_three_fields_three_words(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'key2', 'key5'], ['cat', 'dogs', 'dog'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 3)

    @patch("parse.callback")
    def test_many_words(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'key2', 'key3', 'key5'], ['cat', 'small', 'big'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 4)


if __name__ == '__main__':
    unittest.main()
