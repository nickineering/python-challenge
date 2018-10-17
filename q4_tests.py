"""
Tests question 4
"""
from unittest import TestCase
import unittest
from unittest import mock
from q4 import crawl_links
from q4 import headers

# URLs to use in the test. These could be expanded upon if more elaborate tests were required in future.
test_href = "https://example.com/"
test_image = "/img/logo.jpg"
test_search_url = "https://google.com/"


# This function will be used by the mock to replace requests.get. This prevents network usage so that the test always
# works the same regardless of the state of the developer's network.
def mocked_requests_get(*args, **kwargs):
    # A very simple replacement of the result of requests.get.
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    # A test link and image are included so that their existence can be checked later.
    return MockResponse('I am a test page. <a href="' + test_href + '"/>My Link</a>. <img src="' + test_image +
                        '"> More text.', 200)


# The class that conducts the tests.
class TestCrawlLinks(TestCase):

    # We patch 'requests.get' with our own method. The mock object is passed in to our test case method.
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def setUp(self, mock_get):
        self.data = crawl_links(test_search_url)
        self.mock_get = mock_get

    # Checks that crawl_links returns a valid dictionary.
    def test_fetch_returns_dict(self):
        self.assertTrue(isinstance(self.data, dict))

    # Checks that crawl_links fetches the URL it was supposed to fetch.
    def test_correct_url_searched(self):
        self.assertIn(mock.call(test_search_url, headers=headers, timeout=5), [*self.mock_get.call_args_list])

    # Checks that the test link was found.
    def test_link_found(self):
        self.assertIn(test_href, self.data[test_search_url]["links"])

    # Checks that the test image was found.
    def test_image_found(self):
        self.assertIn(test_image, self.data[test_search_url]["images"])

    # Checks that extra links are not accidentally added to the result.
    def test_correct_num_links_found(self):
        self.assertEqual(1, len(self.data[test_search_url]["links"]))

    # Checks that extra images are not accidentally added to the result.
    def test_correct_num_images_found(self):
        self.assertEqual(1, len(self.data[test_search_url]["images"]))


# Runs the tests if this module is executed directly.
if __name__ == '__main__':
    unittest.main()
