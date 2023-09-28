#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept
curl -sI "$1" | grep -iF "Allow" | sed s/"Allow: "//
