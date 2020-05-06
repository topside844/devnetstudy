from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token='')
memberships = api.memberships.list(roomId='Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli')

with open("devnet-room-membership.csv", "w") as csv_file:    
    for membership in memberships:
        csv_file.write(membership.personDisplayName + "," + membership.personEmail + '\n')