#!/usr/bin/python3
"""Python script that POST an email """
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    payload = {"email": sys.argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
