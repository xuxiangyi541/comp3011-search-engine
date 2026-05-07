import unittest
from src.indexer import build_index

class TestIndexer(unittest.TestCase):

    def test_build_index_basic(self):
        pages = {
            "url1": "hello world",
            "url2": "hello python"
        }

        index = build_index(pages)

        self.assertIn("hello", index)
        self.assertIn("world", index)
        self.assertIn("python", index)

        self.assertIn("url1", index["hello"])
        self.assertIn("url2", index["hello"])

    def test_positions(self):
        pages = {
            "url1": "a b a"
        }

        index = build_index(pages)

        self.assertEqual(index["a"]["url1"], [0, 2])
        self.assertEqual(index["b"]["url1"], [1])


if __name__ == "__main__":
    unittest.main()