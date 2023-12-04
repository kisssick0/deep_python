import unittest
import cjson
import json
from faker import Faker


class TestJsonDumps(unittest.TestCase):
    def test_cjson_vs_json_dumps(self):
        json_dict = {"hello": 10, "world": "value"}
        json_doc = json.dumps(json_dict)
        cjson_doc = cjson.dumps(json_dict)
        self.assertEqual(json_doc, cjson_doc)

    def test_cjson_json_dumps_loads(self):
        json_dict = {"hello": 10, "world": "value"}
        self.assertEqual(json_dict, cjson.loads(cjson.dumps(json_dict)))

    def test_dict_unchanged(self):
        json_dict = {"hello": 10, "world": "value"}
        cjson.dumps(json_dict)
        self.assertEqual({"hello": 10, "world": "value"}, json_dict)

    def test_incorrect_value(self):
        json_dict1 = {"hello": [10, 20], "world": "value"}
        json_dict2 = {"hello": 10, "world": ["value"]}
        with self.assertRaises(TypeError):
            cjson.dumps(json_dict1)
            cjson.dumps(json_dict2)

    def test_incorrect_key(self):
        json_dict = {10: "hello", "world": "value"}
        with self.assertRaises(TypeError):
            cjson.dumps(json_dict)

    def test_incorrect_input_value(self):
        json_str = '{"hello": 10, "world": "value"}'
        with self.assertRaises(TypeError):
            cjson.dumps(json_str)


class TestJsonLoads(unittest.TestCase):
    def test_cjson_vs_json_loads(self):
        json_str = '{"hello": 10, "world": "value"}'
        json_doc = json.loads(json_str)
        cjson_doc = cjson.loads(json_str)
        self.assertEqual(json_doc, cjson_doc)

    def test_cjson_json_loads_dumps(self):
        json_str = '{"hello": 10, "world": "value"}'
        self.assertEqual(json_str, cjson.dumps(cjson.loads(json_str)))

    def test_str_unchanged(self):
        json_str = '{"hello": 10, "world": "value"}'
        cjson.loads(json_str)
        self.assertEqual('{"hello": 10, "world": "value"}', json_str)

    def test_incorrect_value(self):
        json_str1 = '{"hello": [10, 20], "world": "value"}'
        json_str2 = '{"hello": 10, "world": ["value"]}'
        json_str3 = '{"hello": 10abc, "world": "value"}'
        with self.assertRaises(TypeError):
            cjson.loads(json_str1)
            cjson.loads(json_str2)
            cjson.loads(json_str3)

    def test_incorrect_key(self):
        json_str = '{10: "hello", "world": "value"}'
        with self.assertRaises(TypeError):
            cjson.loads(json_str)

    def test_incorrect_input_value(self):
        json_dict = {"hello": 10, "world": "value"}
        with self.assertRaises(TypeError):
            cjson.loads(json_dict)


if __name__ == "__main__":
    unittest.main()
