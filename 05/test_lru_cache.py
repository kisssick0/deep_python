import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(2)
        self.cache.set("k1", "val1")
        self.cache.set("k2", "val2")

    def test_set_get(self):
        self.assertEqual(self.cache.get("k1"), "val1")
        self.assertEqual(self.cache.get("k2"), "val2")

    def test_update_value(self):
        self.assertEqual(self.cache.get("k1"), "val1")
        self.assertEqual(self.cache.get("k2"), "val2")

        self.cache.set("k1", "val111")
        self.assertEqual(self.cache.get("k1"), "val111")
        self.assertEqual(self.cache.get("k2"), "val2")

        self.cache.set("k1", "val1111")
        self.cache.set("k2", "val222")
        self.assertEqual(self.cache.get("k1"), "val1111")
        self.assertEqual(self.cache.get("k2"), "val222")


    def test_missing_key(self):
        self.assertIsNone(self.cache.get("k3"))

        self.cache.set("k3", "val3")
        self.assertEqual(self.cache.get("k3"), "val3")

    def test_reaching_the_limit(self):
        self.assertEqual(self.cache.get("k1"), "val1")
        self.assertEqual(self.cache.get("k2"), "val2")

        self.cache.set("k3", "val3")
        self.assertIsNone(self.cache.get("k1"))

        self.assertEqual(self.cache.get("k2"), "val2")


if __name__ == '__main__':
    unittest.main()
