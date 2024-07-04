#!/bin/bash
# Bash scripts that sending a POST request to a given URL.
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
