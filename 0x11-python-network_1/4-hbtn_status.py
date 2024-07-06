#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status and prints information about the response."""

# Import the requests module, which allows us to send HTTP requests in Python
import requests

# The main function to execute the code block when the script is run directly
if __name__ == "__main__":
    # Send a GET request to the specified URL and store the response in the variable 'r'
    r = requests.get("https://intranet.hbtn.io/status")
    
    # Print the header for the body response
    print("Body response:")
    
    # Print the type of the response content
    print("\t- type: {}".format(type(r.text)))
    
    # Print the actual content of the response
    print("\t- content: {}".format(r.text))
