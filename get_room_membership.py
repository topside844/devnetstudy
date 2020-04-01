import requests

URL = 'https://api.ciscospark.com/v1/memberships'
ACCESS_TOKEN = 'ZGEwYzIyZjUtNzkxNi00YWVmLTkyYjktODBlMDQ3YWNiNDJhNWY3ZGE2NjYtNDI2_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f'
ROOM_ID = 'Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli'


headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
           'Content-type': 'application/json;charset=utf-8'}
post_data = {'roomId': ROOM_ID}

response = requests.get(URL, params=post_data, headers=headers)
if response.status_code == 200:
    # Great your message was posted!
    # message_id = response.json['id']
    # message_text = response.json['text']
    #print("New message created, with ID:", message_id)
    data = response.json()["items"]

    with open("devnet-room-membership.csv", "w") as csv_file:
        for person in data:
            csv_file.write(person["personDisplayName"] + "," + person["personEmail"] + '\n')
    
else:
    # Oops something went wrong...  Better do something about it.
    print(response.status_code, response.text)