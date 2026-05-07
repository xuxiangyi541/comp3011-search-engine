import unittest
from src.search import find

class TestSearch(unittest.TestCase):

    def setUp(self):
        self.index = {
            "hello": {
                "url1": [0],
                "url2": [1]
            },
            "world": {
                "url1": [1]
            }
        }

    def test_single_word(self):
        result = find(self.index, "hello")
        self.assertIn("url1", result)
        self.assertIn("url2", result)

    def test_multiple_words(self):
        result = find(self.index, "hello world")
        self.assertEqual(result, ["url1"])

    def test_word_not_found(self):
        result = find(self.index, "python")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()