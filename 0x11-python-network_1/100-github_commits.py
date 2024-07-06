#!/usr/bin/python3
"""
Lists the 10 recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests

# Check if the script is being run directly
if __name__ == "__main__":
    # Construct the GitHub API URL using command line arguments
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    # Send a GET request to the constructed URL
    r = requests.get(url)

    # Parse the JSON response
    commits = r.json()

    try:
        # Loop through the first 10 commits
        for i in range(10):
            # Print the commit SHA and author name for each commit
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        # Handle the case where there are fewer than 10 commits
        pass
