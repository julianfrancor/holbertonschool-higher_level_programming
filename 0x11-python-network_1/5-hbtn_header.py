#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import sys
import requests


url = sys.argv[1]
r = requests.get(url)
print(r.headers['X-Request-Id'])
