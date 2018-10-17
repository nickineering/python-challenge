#!/usr/bin/env python
"""
Objective: Write a small self contained python command line tool that receives a list of URLs as command line arguments,
and returns a structured JSON data containing all the links and image urls within the document. The tool should be
generic enough to work with any URL. Don't spend more than an hour or two on this. The result should include everything
to make it usable (requirements file, etc.), and tests to ensure it works as expected.

It should be executed as:

>> ./mytool http://example.com http://bbc.co.uk

And return:

{
    "http://example.com": {
        "links": [
            "https://example.link1.com",
            "https://example.link2.com"
        ],
        "images": [
            "https://example.link.com/image/one.jpg",
            "https://example.link.com/images/two.png"
        ]
    },
    "http://bbc.co.uk": {
        .....
    }
}
"""

# This script requires execution permission via the OS to run as a shell script.

import sys
import requests
from bs4 import BeautifulSoup
import json

# A fake header so that our request does not appear suspicious to the sites crawled
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/53.0.2785.143 Safari/537.36'
}


# Crawl the provided list of URLs and extract their links and images. Returns the result in a dictionary.
def crawl_links(urls):
    # If only a single URL pack it into a list so that its string does not get separated by character.
    if not isinstance(urls, list):
        urls = [urls]
    # Create an empty return result to add to later.
    results = {}
    for url in urls:
        # Regardless of whether anything is found in this url create this data structure so reading it later is easier.
        results[url] = {'links': [], 'images': [], 'errors': []}

        # Try to load the URL.
        try:
            page = requests.get(url, headers=headers, timeout=5)
        # Store any exceptions in the errors list.
        except requests.exceptions.RequestException as e:
            results[url]['errors'].append([str(e)])
            return results
        # Note if a request failed because the user quit.
        except KeyboardInterrupt:
            results[url]['errors'].append("Keyboard interrupt exception")
            return results

        # If the page is not okay store its error code and return instead of parsing the error page.
        if page.status_code != 200:
            results[url]['errors'].append("HTTP status " + page.status_code)
            return results

        # Parse the HTML.
        soup = BeautifulSoup(page.text, 'html.parser')

        # Add the links and the images on the page to the final result.
        for link in soup.find_all('a'):
            results[url]['links'].append(link.get('href'))
        for image in soup.find_all('img'):
            results[url]['images'].append(image.get('src'))

    # Return the final result.
    return results


# Runs the example output if and only if the scripts is being executed directly. If it is imported do not run since
# such output might then be an inconvenience.
if __name__ == '__main__':
    # Take the arguments given with the script when it is executed and use them to run crawl_links.
    links = crawl_links(sys.argv[1:])
    # Print the output of crawl_links in JSON form.
    print(json.dumps(links, sort_keys=True, indent=4))
