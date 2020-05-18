import constants
from webexteamssdk import WebexTeamsAPI

'''
# constants.py
BOT_TOKEN = ''
DEMO_ROOM_NAME = '{YOUR_NAME}-DEVNET-TEST'
INVITE_USERNAME = 'user@domain'
'''

teams_api = WebexTeamsAPI(access_token=constants.BOT_TOKEN)

# Create a room (space) and name it "{YOUR_NAME}-DEVNET-TEST"
demo_room = teams_api.rooms.create(constants.DEMO_ROOM_NAME)

# Invite your own Webex Teams user to the room you created.
teams_api.memberships.create(demo_room.id, personEmail=constants.INVITE_USERNAME)

# Post a message to the room that warmly welcomes your Webex Teams user.
user_search = teams_api.people.list(email=constants.INVITE_USERNAME)
for user in user_search:
    message = teams_api.messages.create(roomId=demo_room.id, text=f'Welcome {user.displayName}')
