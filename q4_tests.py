from unittest import TestCase
import unittest
from q4 import crawl_links


class test_crawl_links(TestCase):
    def test_connects(self):
            self.assertIsNotNone(crawl_links("https://google.com"))


if __name__ == '__main__':
    unittest.main()
