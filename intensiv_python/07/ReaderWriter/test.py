import unittest
import io
from Reader import TxtReader, CsvReader, JsonReader
from Writer import TxtWriter, CsvWriter, JsonWriter


class TestAnograms(unittest.TestCase):
    def test_readers(self):
        with open('test_readers/test.txt', 'r', encoding='utf-8') as fileobj:
            lines = TxtReader.read(fileobj)
            correct_result = [
                "123\n",
                "asdf asdf\n",
                "1+1+1=3"
            ]
            self.assertListEqual(lines, correct_result)
            self.assertEqual(fileobj.closed, True)

        with open('test_readers/test.csv', 'r', encoding='utf-8') as fileobj:
            lines = CsvReader.read(fileobj)
            correct_result = [
                "123 road road",
                "!road 123 123",
                "123 road road",
                "!road 123 123"
            ]
            self.assertListEqual(lines, correct_result)
            self.assertEqual(fileobj.closed, True)

        with open('test_readers/test.json', 'r', encoding='utf-8') as fileobj:
            lines = JsonReader.read(fileobj)
            correct_result = {
                "name": "John",
                "age": 30,
                "car": None
            }
            self.assertDictEqual(lines, correct_result)
            self.assertEqual(fileobj.closed, True)

    def test_reader_mode(self):
        with open('test_readers/test_mode.txt',
                  'w', encoding='utf-8') as fileobj:
            try:
                self.assertRaises(io.UnsupportedOperation,
                                  TxtReader.read(fileobj))
            except io.UnsupportedOperation:
                pass

        with open('test_readers/test_mode.csv',
                  'w', encoding='utf-8') as fileobj:
            try:
                self.assertRaises(io.UnsupportedOperation,
                                  CsvReader.read(fileobj))
            except io.UnsupportedOperation:
                pass

        with open('test_readers/test_mode.json',
                  'w', encoding='utf-8') as fileobj:
            try:
                self.assertRaises(io.UnsupportedOperation,
                                  JsonReader.read(fileobj))
            except io.UnsupportedOperation:
                pass

    def test_write(self):
        with open('test_writers/test.txt', 'w', encoding='utf-8') as fileobj:
            data = ['а Роза упала на лапу Азора', 'а Роза упала на лапу Азора']
            TxtWriter.dump(data, fileobj)

        with open('test_writers/test.txt', 'r', encoding='utf-8') as fileobj:
            lines = TxtReader.read(fileobj)
            data[0] += '\n'
            data[1] += '\n'
            self.assertListEqual(lines, data)

        with open('test_writers/test.txt', 'w', encoding='utf-8') as fileobj:
            data = 'а Роза упала на лапу Азора'
            TxtWriter.dump(data, fileobj)

        with open('test_writers/test.txt', 'r', encoding='utf-8') as fileobj:
            lines = TxtReader.read(fileobj)
            self.assertListEqual(lines, [data])

        with open('test_writers/test.csv', 'w', encoding='utf-8') as fileobj:
            data = ['123 123 123',
                    '123 123 123',
                    '123 123 123',
                    '123 123 123']
            CsvWriter.dump(data, fileobj)

        with open('test_writers/test.csv', 'r', encoding='utf-8') as fileobj:
            lines = CsvReader.read(fileobj)
            self.assertListEqual(lines, data)

        with open('test_writers/test.csv', 'w', encoding='utf-8') as fileobj:
            data = '123 123 123'
            CsvWriter.dump(data, fileobj)

        with open('test_writers/test.csv', 'r', encoding='utf-8') as fileobj:
            lines = CsvReader.read(fileobj)
            self.assertListEqual(lines, [data])

        with open('test_writers/test.json', 'w', encoding='utf-8') as fileobj:
            data = {"x": "1"}
            JsonWriter.dump(data, fileobj)

        with open('test_writers/test.json', 'r', encoding='utf-8') as fileobj:
            lines = JsonReader.read(fileobj)
            self.assertDictEqual(lines, data)

        with open('test_writers/test.json', 'w', encoding='utf-8') as fileobj:
            data = '{"x": "1"}'
            JsonWriter.dump(data, fileobj)

        with open('test_writers/test.json', 'r', encoding='utf-8') as fileobj:
            lines = JsonReader.read(fileobj)
            self.assertDictEqual(lines, {"x": "1"})

    def test_writer_mode(self):
        with open('test_writers/test.txt', 'r', encoding='utf-8') as fileobj:
            data = ['а Роза упала на лапу Азора', 'а Роза упала на лапу Азора']
            try:
                self.assertRaises(io.UnsupportedOperation,
                                  TxtWriter.dump(data, fileobj))
            except io.UnsupportedOperation:
                pass

        with open('test_writers/test.csv', 'r', encoding='utf-8') as fileobj:
            data = ['123 123 123', '123 123 123']
            try:
                self.assertRaises(io.UnsupportedOperation,
                                  CsvWriter.dump(data, fileobj))
            except io.UnsupportedOperation:
                pass

        with open('test_writers/test.json', 'r', encoding='utf-8') as fileobj:
            data = {"x": "1"}
            try:
                self.assertRaises(io.UnsupportedOperation,
                                  JsonWriter.dump(data, fileobj))
            except io.UnsupportedOperation:
                pass

    def test_writer_argument(self):
        with open('test_writers/test.txt', 'w', encoding='utf-8') as fileobj:
            data = {"x": "1"}
            try:
                self.assertRaises(TypeError, TxtWriter.dump(data, fileobj))
            except TypeError:
                pass

        with open('test_writers/test.csv', 'w', encoding='utf-8') as fileobj:
            data = {"x": "1"}
            try:
                self.assertRaises(TypeError, CsvWriter.dump(data, fileobj))
            except TypeError:
                pass

        with open('test_writers/test.json', 'w', encoding='utf-8') as fileobj:
            data = ['а Роза упала на лапу Азора', 'а Роза упала на лапу Азора']
            try:
                self.assertRaises(TypeError, JsonWriter.dump(data, fileobj))
            except TypeError:
                pass


if __name__ == "__main__":
    unittest.main()
