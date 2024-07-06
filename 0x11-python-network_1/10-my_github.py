#!/usr/bin/python3
"""Sening a search request for a certain string to the Star Wars API.

Usage: ./9-starwars.py <search string>
  - Sending serach request to the Star Wars API search people endpoint.
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://swapi.co/api/people"
    params = {"search": sys.argv[1]}
    results = requests.get(url, params=params).json()

    print("Number of results: {}".format(results.get("count")))
    [print(r.get("name")) for r in results.get("results")]
