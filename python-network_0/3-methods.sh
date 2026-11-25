#!/bin/bash
# Displays all the HTTP methods the server at a URL accepts
curl -sI -X OPTIONS "$1" | grep -i '^allow:' | cut -d ' ' -f 2- | tr -d '\r'
