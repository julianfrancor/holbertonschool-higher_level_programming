#!/usr/bin/python3
"""Python script that takes in a URL and an email, sends a POST request
 to the passed URL with the email as a parameter, and displays the body
 of the response (decoded in utf-8)"""
import sys
import urllib.request


def function_to_fetch():
    "Function that fetches a URL"
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('utf-8')
    url = sys.argv[1]
    with urllib.request.urlopen(url, data) as response:
        body = response.read()
        print(body.decode('utf-8'))

if __name__ == "__main__":
    function_to_fetch()
