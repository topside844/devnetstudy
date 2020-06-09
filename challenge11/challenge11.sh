#!/bin/bash

# Use an operating system environment variable to store your bearer token (i.e. WEBEX_TEAMS_ACCESS_TOKEN)
# Use "curl" to retrieve your current status and save the result to a file (i.e. response.txt)
curl -s -X GET -H "Authorization: Bearer $WEBEX_TEAMS_ACCESS_TOKEN" https://webexapis.com/v1/people/me > response.txt

# Strip the status out of the output.
jq -r '.status' response.txt > status.txt

# Use "curl" to post the status you read from status.txt into the Webex Teams Room id: Y2lzY29zcGFyazovL3VzL1JPT00vMDg5ZDNiMTAtYTc2Yy0xMWVhLWJhMjQtZjE0NTA4YWE0ODIw
curl -X POST -H "Authorization: Bearer $WEBEX_TEAMS_ACCESS_TOKEN" -H "Content-Type: application/json" --data '{"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vODE5NDliZjAtOThjOS0xMWVhLTg0YWQtNTU5ZmM5OThhNTE2","text":"'"$(<status.txt)"'"}' https://webexapis.com/v1/messages
