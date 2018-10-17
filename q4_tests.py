from unittest import TestCase
import unittest
from unittest import mock
from q4 import crawl_links


# This method will be used by the mock to replace requests.get
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    return MockResponse('I am a test page', 200)


# Our test case class
class TestCrawlLinks(TestCase):

    # def test_connects(self):
    #         self.assertIsNotNone(crawl_links("https://google.com"))

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_fetch(self, mock_get):
        # Assert requests.get calls
        test_url = "https://google.com"
        data = crawl_links(test_url)
        self.assertTrue(isinstance(data, dict))
        # json_data = mgc.fetch_json('http://someotherurl.com/anothertest.json')
        # self.assertEqual(json_data, {"key2": "value2"})
        # json_data = mgc.fetch_json('http://nonexistenturl.com/cantfindme.json')
        # self.assertIsNone(json_data)
        self.assertIn(mock.call(test_url), mock_get.call_args_list)


if __name__ == '__main__':
    unittest.main()
