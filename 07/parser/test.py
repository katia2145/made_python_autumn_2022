import unittest
from my_parser import parser


class TestAnograms(unittest.TestCase):

    def test_exist_file(self):
        fileobj = open("example.txt", "r", encoding='utf-8')
        result = parser(fileobj, ["пророк", "он"])
        correct_result = ['моих зениц коснулся он.',
                          'моих ушей коснулся он, —',
                          'и он к устам моим приник,',
                          'и он мне грудь рассек мечом,',
                          '«восстань, пророк, и виждь, и внемли,']
        self.assertListEqual(result, correct_result)
        self.assertEqual(fileobj.closed, True)

        file_path = "example.txt"
        result = parser(file_path, ["пророк", "он"])
        correct_result = ['моих зениц коснулся он.',
                          'моих ушей коснулся он, —',
                          'и он к устам моим приник,',
                          'и он мне грудь рассек мечом,',
                          '«восстань, пророк, и виждь, и внемли,']
        self.assertListEqual(result, correct_result)

        file_path = "example.txt"
        result = parser(file_path, ["роза"])
        self.assertListEqual(result, [])

        file_path = "example.txt"
        result = parser(file_path, [])
        self.assertListEqual(result, [])

    def test_throw_ecxeption(self):
        try:
            fileobj = open("first_example.txt", "r", encoding='utf-8')
            self.assertRaises(FileNotFoundError,
                              parser(fileobj, ["пророк", "он"]))
        except FileNotFoundError:
            pass

        try:
            self.assertRaises(FileNotFoundError,
                              parser("first_example.txt", ["пророк", "он"]))
        except FileNotFoundError:
            pass

        try:
            self.assertRaises(TypeError, parser([], ["пророк", "он"]))
        except TypeError:
            pass


if __name__ == "__main__":
    unittest.main()
