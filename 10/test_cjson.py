import unittest
import json
import cjson


class TestJsonLoads(unittest.TestCase):
    def test_cjson_usual_loads(self):
        json_str = '{"nickname": "kisssick"}'
        json_dict = json.loads(json_str)
        cjson_dict = cjson.loads(json_str)
        self.assertEqual(json_dict, cjson_dict)

        json_str = '{"number": 47}'
        json_dict = json.loads(json_str)
        cjson_dict = cjson.loads(json_str)
        self.assertEqual(json_dict, cjson_dict)

        json_str = '{"nickname": "kisssick", "number": 47}'
        json_dict = json.loads(json_str)
        cjson_dict = cjson.loads(json_str)
        self.assertEqual(json_dict, cjson_dict)

    def test_cjson_loads_str_equal(self):
        json_str = '{"nickname": "kisssick", "number": 47}'
        cjson.loads(json_str)
        self.assertEqual('{"nickname": "kisssick", "number": 47}', json_str)

    def test_cjson_loads_incorrect_type(self):
        example_num = 6
        with self.assertRaises(TypeError):
            cjson.loads(example_num)

        example_dict = {"nickname": "kisssick", "number": 47}
        with self.assertRaises(TypeError):
            cjson.loads(example_dict)

    def test_cjson_loads_incorrect_key(self):
        json_str = '{"nickname": "kissick", 47: "number"}'
        with self.assertRaises(TypeError):
            cjson.loads(json_str)

    def test_cjson_loads_incorrect_value(self):
        json_str1 = '{"something": [47, 74], "nickname": "kissick", "number": 47}'
        json_str2 = '{"something": "47", "nickname": ["kissick"], "number": 47}'
        json_str3 = '{"something": 47ki, "nickname": "kissick", "number": 47}'

        with self.assertRaises(TypeError):
            cjson.loads(json_str1)
            cjson.loads(json_str2)
            cjson.loads(json_str3)


class TestCjsonDumps(unittest.TestCase):
    def test_cjson_correct_dumps(self):
        json_dict = {"nickname": "kisssick"}
        json_str = json.dumps(json_dict)
        cjson_str = cjson.dumps(json_dict)
        self.assertEqual(json_str, cjson_str)

        json_dict = {"number": 47}
        json_str = json.dumps(json_dict)
        cjson_str = cjson.dumps(json_dict)
        self.assertEqual(json_str, cjson_str)

        json_dict = {"nickname": "kisssick", "number": 47}
        json_str = json.dumps(json_dict)
        cjson_str = cjson.dumps(json_dict)
        self.assertEqual(json_str, cjson_str)

    def test_cjson_dumps_dict_equal(self):
        json_dict = {"nickname": "kisssick", "number": 47}
        cjson.dumps(json_dict)
        self.assertEqual({"nickname": "kisssick", "number": 47}, json_dict)

    def test_cjson_dumps_incorrect_type(self):
        number = 47
        with self.assertRaises(TypeError):
            cjson.dumps(number)

        json_str = '{"something": [47, 74], "nickname": "kissick", "number": 47}'
        with self.assertRaises(TypeError):
            cjson.dumps(json_str)

    def test_cjson_dumps_incorrect_key(self):
        json_dict = {"nickname": "kissick", 47: "number"}
        with self.assertRaises(TypeError):
            cjson.dumps(json_dict)

    def test_cjson_dumps_incorrect_value(self):
        json_dict1 = {"something": [47, 74], "nickname": "kissick", "number": 47}
        json_dict2 = {"something": "47", "nickname": ["kissick"], "number": 47}

        with self.assertRaises(TypeError):
            cjson.dumps(json_dict1)
            cjson.dumps(json_dict2)


class TestCjson(unittest.TestCase):
    def test_cjson_dumps_loads(self):
        example_dict = {"nickname": "kisssick"}
        cjson_loaded_dict = cjson.loads(cjson.dumps(example_dict))
        self.assertEqual(example_dict, cjson_loaded_dict)

        example_dict = {"number": 47}
        cjson_loaded_dict = cjson.loads(cjson.dumps(example_dict))
        self.assertEqual(example_dict, cjson_loaded_dict)

        example_dict = {"nickname": "kisssick", "number": 47}
        cjson_loaded_dict = cjson.loads(cjson.dumps(example_dict))
        self.assertEqual(example_dict, cjson_loaded_dict)


if __name__ == "__main__":
    unittest.main()
