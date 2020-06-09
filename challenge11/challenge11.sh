#!/bin/bash

# Use an operating system environment variable to store your bearer token (i.e. WEBEX_TEAMS_ACCESS_TOKEN)
# Use "curl" to retrieve your current status and save the result to a file (i.e. response.txt)

curl -s -D -X GET https://webexapis.com/v1/people/me -H "Authorization: Bearer $WEBEX_TEAMS_ACCESS_TOKEN" | json_pp > response.txt

# Note: The status is in a request that includes a lot more data than just your status. That is ok.
# Strip the status out of the output.
# This is a little advanced, so feel free to use the code below where "response.txt" is the same as whatever you used in step 2
# grep status response.txt | awk -F 'status' '{ print $2 }' | awk -F '"' '{ print $3 }' >> status.txt
# Use "curl" to post the status you read from status.txt into the Webex Teams Room id: Y2lzY29zcGFyazovL3VzL1JPT00vMDg5ZDNiMTAtYTc2Yy0xMWVhLWJhMjQtZjE0NTA4YWE0ODIw
# Note: There are many ways to accomplish this. Feel free to solve this however you like. Also, please reach out to myself, David, Jason, Brad, Patrick etc if you get stuck!
