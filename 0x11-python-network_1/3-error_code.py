#!/usr/bin/python3
"""Sends a request to a paticular URL and shows the response body.

Usage: ./3-error_code.py <URL>
  - Handles HTTP errors and prints the error code if it occurs.
"""
import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    # Create a request object with the provided URL
    request = urllib.request.Request(url)
    
    try:
        # Send the request and handle the response
        with urllib.request.urlopen(request) as response:
            # Print the response body as ASCII text
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        # If an HTTP error occurs, print the error code
        print("Error code: {}".format(e.code))
