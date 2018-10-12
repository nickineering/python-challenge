from unittest import TestCase
import unittest
from collections.abc import Iterable


data = [
    'one',
    ['one', 'two'],
    {'one': 1, 'two': 2},
    1
]


def to_list(args):
    if isinstance(args, str) or not isinstance(args, Iterable):
        args = [args]
    return [*args]


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
    for datum in data:
        print(str(to_list(datum)))
    unittest.main()
