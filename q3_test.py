from unittest import TestCase
import unittest
from q3 import data
from q3 import create_dict


class ListTest(TestCase):
    def test_returns_dict(self):
            self.assertTrue(isinstance(create_dict(data['x'], data['y']), dict))


if __name__ == '__main__':
    unittest.main()
