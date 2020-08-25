#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter """
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = {'q': sys.argv[1]}
    else:
        letter = {'q': ""}
    r = requests.post(url, letter)
    try:
        """there is a decoder for JSON incorporated in Requests"""
        answer = r.json()
        if answer is not None:
            print("[{}] {}".format(answer['id'], answer['name']))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
