import unittest
from LRUCache import LRUCache


class TestSalary(unittest.TestCase):
    def test_LRUCache(self):
        cache = LRUCache(2)

        cache.set("k1", "val1")
        cur_priority = {"k1": 1}
        cur_values = {"k1": "val1"}
        self.assertDictEqual(cur_priority, cache.priority)
        self.assertDictEqual(cur_values, cache.values)

        cache.set("k2", "val2")
        cur_priority = {"k1": 1, "k2": 2}
        cur_values = {"k1": "val1", "k2": "val2"}
        self.assertDictEqual(cur_priority, cache.priority)
        self.assertDictEqual(cur_values, cache.values)

        result = cache.get("k3")
        self.assertIsNone(result)

        result = cache.get("k2")
        self.assertEqual(result, "val2")
        cur_priority = {"k1": 1, "k2": 3}
        self.assertDictEqual(cur_priority, cache.priority)

        result = cache.get("k1")
        self.assertEqual(result, "val1")
        cur_priority = {"k1": 4, "k2": 3}
        self.assertDictEqual(cur_priority, cache.priority)

        cache.set("k3", "val3")
        cur_priority = {"k1": 4, "k3": 5}
        cur_values = {"k1": "val1", "k3": "val3"}
        self.assertDictEqual(cur_priority, cache.priority)
        self.assertDictEqual(cur_values, cache.values)

        result = cache.get("k2")
        self.assertIsNone(result)

        result = cache.get("k1")
        self.assertEqual(result, "val1")
        cur_priority = {"k1": 6, "k3": 5}
        self.assertDictEqual(cur_priority, cache.priority)

        cache.set("k3", "val33")
        cur_priority = {"k1": 6, "k3": 7}
        cur_values = {"k1": "val1", "k3": "val33"}
        self.assertDictEqual(cur_priority, cache.priority)
        self.assertDictEqual(cur_values, cache.values)

        result = cache.get("k1")
        self.assertEqual(result, "val1")
        cur_priority = {"k1": 8, "k3": 7}
        self.assertDictEqual(cur_priority, cache.priority)

        cache.set("k4", "val4")
        cur_priority = {"k1": 8, "k4": 9}
        cur_values = {"k1": "val1", "k4": "val4"}
        self.assertDictEqual(cur_priority, cache.priority)
        self.assertDictEqual(cur_values, cache.values)

        result = cache.get("k3")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
