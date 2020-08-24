#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response."""
import sys
import urllib.request


def function_to_fetch():
    "Function that fetches a URL"
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.info()
        print(header['X-Request-Id'])

if __name__ == "__main__":
    function_to_fetch()
