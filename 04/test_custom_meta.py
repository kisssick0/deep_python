import unittest
from custom_meta import CustomClass


class TestMetaClass(unittest.TestCase):
    def test_class_instance(self):
        inst = CustomClass()
        self.assertTrue(inst.custom_x == 50)
        self.assertTrue(inst.custom_val == 99)
        self.assertTrue(inst.custom_line() == 100)
        self.assertTrue(str(inst) == "Custom_by_metaclass")

    def test_class_attr(self):
        self.assertTrue(CustomClass.custom_x == 50)

    def test_dynamic(self):
        inst = CustomClass()
        inst.dynamic = "aaa"
        CustomClass.foo = 1
        self.assertTrue(inst.custom_dynamic == "aaa")
        self.assertEqual(CustomClass.custom_foo, 1)
        with self.assertRaises(AttributeError):
            inst.dynamic
        with self.assertRaises(AttributeError):
            CustomClass.foo

    def test_errors(self):
        inst = CustomClass()
        inst_x = lambda: inst.x
        inst_val = lambda: inst.val
        inst_line = lambda: inst.line()
        inst_aaa = lambda: inst.aaa
        class_x = lambda: CustomClass.x
        self.assertRaises(AttributeError, inst_x)
        self.assertRaises(AttributeError, inst_val)
        self.assertRaises(AttributeError, inst_line)
        self.assertRaises(AttributeError, inst_aaa)
        self.assertRaises(AttributeError, class_x)


if __name__ == '__main__':
    unittest.main()
