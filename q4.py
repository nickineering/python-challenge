#!/usr/bin/env python
import sys
import requests
from bs4 import BeautifulSoup as BS
import json


def crawl_links(urls):
    results = {}
    for url in urls:
        results[url] = {'links': [], 'images': []}
        try:
            page = requests.get(url)
            soup = BS(page.text, 'html.parser')

            for link in soup.find_all('a'):
                results[url]['links'].append(link.get('href'))
            for image in soup.find_all('img'):
                results[url]['images'].append(image.get('src'))

        except requests.exceptions.RequestException as e:
            results[url]['errors'] = [str(e)]

    return results


if __name__ == '__main__':
    links = crawl_links(sys.argv[1:])
    print(json.dumps(links, sort_keys=True, indent=4))
