#!/usr/bin/python3
"""Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” You must use
the Github API, here is the documentation
https://developer.github.com/v3/repos/commits/ Print all commits
by: `<sha>: <author name>` (one by line)"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[1], sys.argv[2])
    r = requests.get(url)
    for i in r.json()[0:10]:
        print("{}: {}".format(i.get('sha'), i.get(
            'commit').get('author').get('name')))
