#!/bin/bash
# # Send DELETE request to URL passed as first argument and displays HTTPS response
curl -sX "DELETE" "$1"
