#!/usr/bin/python3
"""Sending a POST request to a certain  URL with a particular email.

Usage: ./2-post_email.py <URL> <email>
  - Shows the response body.
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from command line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email into the format required for a POST request
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Create a POST request with the given URL and data
    request = urllib.request.Request(url, data)

    # Send the request and get the response
    with urllib.request.urlopen(request) as response:
        # Decode the response body to utf-8 and print it
        print(response.read().decode("utf-8"))
