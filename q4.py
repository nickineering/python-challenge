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

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
                  'Chrome/53.0.2785.143 Safari/537.36'
}


def crawl_links(urls):
    if not isinstance(urls, list):
        urls = [urls]
    results = {}
    for url in urls:
        results[url] = {'links': [], 'images': [], 'errors': []}

        try:
            page = requests.get(url, headers=headers, timeout=5)
        except requests.exceptions.RequestException as e:
            results[url]['errors'].append([str(e)])
            return results
        except KeyboardInterrupt:
            results[url]['errors'].append("Keyboard interrupt exception")
            return results

        if page.status_code != 200:
            results[url]['errors'].append("HTTP status " + page.status_code)
            return results

        soup = BeautifulSoup(page.text, 'html.parser')

        for link in soup.find_all('a'):
            results[url]['links'].append(link.get('href'))
        for image in soup.find_all('img'):
            results[url]['images'].append(image.get('src'))

    return results


if __name__ == '__main__':
    links = crawl_links(sys.argv[1:])
    print(json.dumps(links, sort_keys=True, indent=4))
