from unittest import TestCase
import unittest
from unittest import mock
from q4 import crawl_links
from q4 import headers


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    return MockResponse('I am a test page', 200)


# Our test case class
class TestCrawlLinks(TestCase):
    test_url = "https://google.com"

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def setUp(self, mock_get):
        self.data = crawl_links(self.test_url)
        self.mock_get = mock_get

    def test_fetch_returns_dict(self):
        self.assertTrue(isinstance(self.data, dict))

    def test_correct_url_searched(self):
        self.assertIn(mock.call(self.test_url, headers=headers, timeout=5), [*self.mock_get.call_args_list])


if __name__ == '__main__':
    unittest.main()
