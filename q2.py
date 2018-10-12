from unittest import TestCase
import unittest

data = [
    'one',
    ['one', 'two'],
    {'one': 1, 'two': 2}
]


def to_list(input):
    return input


class ListTest(TestCase):
    def test_returns_list(self):
        for datum in data:
            self.assertTrue(isinstance(to_list(datum), list))

    def test_list_full(self):
        for datum in data:
            self.assertGreater(len(to_list(datum)), 0)


if __name__ == '__main__':
    for datum in data:
        print(str(to_list(datum)))
    unittest.main()
