#!/usr/bin/python3
"""Python script that handles Error code """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    bad_r = requests.get(url)
    if bad_r.status_code >= 400:
        print("Error code:", bad_r.status_code)
    else:
        print(bad_r.text)
