#!/usr/bin/env bash
# This script uses curl to send a request to 
# a URL provided as arg and displays
# size of the boyd of the response

# Check if user provided url as arg
if [ $# -ne 1 ]; then
	echo "Usage: 0-body_size.sh URL"
	exit
fi

# Use curl to get headers
headers=$(curl -sI "$1")

# Extracting content length
content_length=$(echo "$headers" | grep -i "Content-Length" | sed 's/Content-Length: //i')

# Printing size
echo "$content_length"
