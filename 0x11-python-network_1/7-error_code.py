#!/usr/bin/python3
"""
Sending request to a particular URL and shows the body of the response.

Usage: ./7-error_code.py <URL>
  - Holds HTTP errors.
"""

import sys  # Importing the sys module to handle command line arguments
import requests  # Importing the requests module to make HTTP requests

# Check if the script is being run directly
if __name__ == "__main__":
    # Retrieve the URL passed as a command line argument
    url = sys.argv[1]

    # Make a GET request to the specified URL
    r = requests.get(url)

    # Check if the response status code indicates an error (400 or higher)
    if r.status_code >= 400:
        # Print the error code
        print("Error code: {}".format(r.status_code))
    else:
        # Print the response body
        print(r.text)
