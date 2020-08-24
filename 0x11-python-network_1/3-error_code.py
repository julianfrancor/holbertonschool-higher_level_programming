#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)."""
import sys
import urllib.request


def error_code_handler():
    "Function that raise an HTTPError"
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print ("Error code: ", e.code)


if __name__ == "__main__":
    error_code_handler()
