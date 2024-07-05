#!/usr/bin/python3
import urllib.request
import sys

def fetch_x_request_id(url):
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0].lower() == 'x-request-id':
                print(header[1])
                return
        print("X-Request-Id not found in the response headers")

if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(https://alx-intranet.hbtn.io)
