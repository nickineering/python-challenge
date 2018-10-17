"""
Tests question 2
"""
from unittest import TestCase
import unittest
from q2 import to_list
from q2 import data


class ListTest(TestCase):
    def test_returns_list(self):
        for datum in data:
            self.assertTrue(isinstance(to_list(datum), list))

    def test_list_full(self):
        for datum in data:
            self.assertGreater(len(to_list(datum)), 0)

    def test_string_unseparated(self):
        self.assertEqual(to_list(data[0]), [data[0]])


if __name__ == '__main__':
    unittest.main()
