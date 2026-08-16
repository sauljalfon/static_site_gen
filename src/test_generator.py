import unittest

from generator import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")

    def test_extract_title_no_hash(self):
        markdown = "Hello"
        with self.assertRaises(ValueError):
            extract_title(markdown)
