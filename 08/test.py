import unittest
from anograms import find_anagrams


class TestAnograms(unittest.TestCase):
    def test_empty_result(self):

        result = find_anagrams('abcd', 'f')
        self.assertEqual(result, [])

        result = find_anagrams('abcd', 'ce')
        self.assertEqual(result, [])

        result = find_anagrams('abcd', '')
        self.assertEqual(result, [])

        result = find_anagrams('', 'ce')
        self.assertEqual(result, [])

    def test_not_empty_result(self):

        result = find_anagrams("abcba", "abc")
        self.assertEqual(result, [0, 2])

        result = find_anagrams("aaa", "a")
        self.assertEqual(result, [0, 1, 2])

        result = find_anagrams("abc cba xabcd", "abc")
        self.assertEqual(result, [0, 4, 9])

        result = find_anagrams("abc", "abc")
        self.assertEqual(result, [0])

        result = find_anagrams("cbacab", "abc")
        self.assertEqual(result, [0, 1, 3])

        result = find_anagrams("aaaa", "aa")
        self.assertEqual(result, [0, 1, 2])


if __name__ == "__main__":
    unittest.main()
