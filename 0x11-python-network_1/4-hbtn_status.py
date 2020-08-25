#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""
import requests


r = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type:", type(r.text))
print("\t- content:", r.text)
