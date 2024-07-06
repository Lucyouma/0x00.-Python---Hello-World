#!/usr/bin/python3
"""
Sends a POST request to a particular URL with a certain email.

Usage: ./6-post_email.py <URL> <email>
  - Shows the body of the response.
"""
import sys
import requests

# Main execution block, ensuring code only runs when script is executed directly
if __name__ == "__main__":
    # Retrieve the URL from the first command line argument
    url = sys.argv[1]
    
    # Retrieve the email from the second command line argument and store it in a dictionary
    value = {"email": sys.argv[2]}
    
    # Send a POST request to the specified URL with the email data
    r = requests.post(url, data=value)
    
    # Print the body of the response received from the POST request
    print(r.text)
