import unittest
import time
from fetcher import start


class TestTicTacGame(unittest.TestCase):
    def test_time(self):
        asyncio_time = time.time()
        start('urls.txt')
        asyncio_time = time.time() - asyncio_time


if __name__ == "__main__":
    unittest.main()
