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

    def test_keyword_callback_is_none(self):
        self.assertIsNone(parse.parse_json(self.json_str, ['key1'], ['cat'], None))

    @patch("parse.callback")
    def test_one_field_one_word(self, callback_mock):
        parse.parse_json(self.json_str, ['key5'], ['dogs'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)
        callback_mock.assert_any_call('key5', 'dogs')

    @patch("parse.callback")
    def test_one_field_two_words(self, callback_mock):
        parse.parse_json(self.json_str, ['key3'], ['big', 'dog'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)
        callback_mock.assert_any_call('key3', 'big')
        callback_mock.assert_any_call('key3', 'dog')

    @patch("parse.callback")
    def test_two_fields_one_word(self, callback_mock):
        parse.parse_json(self.json_str, ['key2', 'key3'], ['dog'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)
        callback_mock.assert_any_call('key2', 'dog')
        callback_mock.assert_any_call('key3', 'dog')

    @patch("parse.callback")
    def test_keywords_register(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'Key1'], ['cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 2)
        callback_mock.assert_any_call('key1', 'cat')
        callback_mock.assert_any_call('Key1', 'cat')

    @patch("parse.callback")
    def test_substring(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'key4'], ['cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)
        callback_mock.assert_any_call('key1', 'cat')

    @patch("parse.callback")
    def test_required_fields_register(self, callback_mock):
        parse.parse_json(self.json_str, ['key1'], ['cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 1)
        callback_mock.assert_any_call('key1', 'cat')

    @patch("parse.callback")
    def test_three_fields_three_words(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'key2', 'key5'], ['cat', 'dogs', 'dog'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 3)
        callback_mock.assert_any_call('key1', 'cat')
        callback_mock.assert_any_call('key5', 'dogs')
        callback_mock.assert_any_call('key2', 'dog')

    @patch("parse.callback")
    def test_many_words(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'key2', 'key3', 'key5'], ['cat', 'small', 'big'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 4)
        callback_mock.assert_any_call('key1', 'small')
        callback_mock.assert_any_call('key1', 'cat')
        callback_mock.assert_any_call('key2', 'small')
        callback_mock.assert_any_call('key3', 'big')

    @patch("parse.callback")
    def test_keyword_not_in_required_fields(self, callback_mock):
        parse.parse_json(self.json_str, ['key1', 'Key1', 'key2', 'key3', 'key4', 'key5'], ['man'], callback_mock)
        self.assertFalse(callback_mock.called)

    @patch("parse.callback")
    def test_many_keywords_in_one_required_field(self, callback_mock):
        parse.parse_json(self.json_str, ['key1'], ['small', 'cat', 'run'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 3)
        callback_mock.assert_any_call('key1', 'small')
        callback_mock.assert_any_call('key1', 'cat')
        callback_mock.assert_any_call('key1', 'run')

    @patch("parse.callback")
    def test_case_insensitive_keyword(self, callback_mock):
        parse.parse_json(self.json_str, ['key1'], ['sMaLl', 'Cat', 'ruN'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 3)
        callback_mock.assert_any_call('key1', 'small')
        callback_mock.assert_any_call('key1', 'cat')
        callback_mock.assert_any_call('key1', 'run')

        parse.parse_json(self.json_str, ['Key1'], ['bIg', 'cat'], callback_mock)
        self.assertTrue(callback_mock.called)
        self.assertEqual(callback_mock.call_count, 5)
        callback_mock.assert_any_call('Key1', 'big')
        callback_mock.assert_any_call('Key1', 'cat')


if __name__ == '__main__':
    unittest.main()
