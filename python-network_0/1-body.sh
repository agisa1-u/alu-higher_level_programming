#!/bin/bash
# Sends a GET request to a URL and displays the body only if the status code is 200
body=$(mktemp)
status=$(curl -s -o "$body" -w '%{http_code}' "$1")
if [ "$status" = "200" ]; then
    cat "$body"
fi
rm -f "$body"
