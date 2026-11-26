#!/usr/bin/python3
"""Script that POSTs an email to a URL and displays the response body."""
import sys
import requests

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
