from webexteamssdk import WebexTeamsAPI
import requests
import re

meraki_api_key = '093b24e85df15a3e66f1fc359f4c48493eaa1b73'
mynetwork = 'L_646829496481100388'

msversion = '11.31'
mrversion = '26.6.1'
mxversion = '15.27'
mvversion = '4.0'
WebexRoomID = "Y2lzY29zcGFyazovL3VzL1JPT00vNWJiMmRiZjAtNmFkOC0xMWVhLWEzNmEtMDc0ZjMxN2Y0Njli"
myWebexToken = "" #you will need to put your personal token here
mscount = mrcount = mxcount = mvcount = 0
bad_devices = []

baseurl = "https://dashboard.meraki.com/api/v0/networks/"

payload = {}
headers = {'X-Cisco-Meraki-API-Key': meraki_api_key} #you will need to look to the meraki_api_key

url = baseurl + mynetwork + "/devices"  #finish the url!

response = requests.get(url, headers = headers) #complete the api call using the requests library

myresponse = response.json()



for device in myresponse:
    firmware = re.sub('\D+(.*)', '\\1', device['firmware'])
    firmware = firmware.replace('-', '.')
    device_type = device['model'][:2]
    
    if (device_type == "MS"):
        if firmware == msversion:
            mscount += 1
        else:
            bad_devices.append(device)
    elif (device_type == "MR"):
        if firmware == mrversion:
            mrcount += 1
        else:
            bad_devices.append(device)
    elif (device_type == "MX"):
        if firmware == mxversion:
            mxcount += 1
        else:
            bad_devices.append(device)            
    elif (device_type == "MV"):
        if firmware == mvversion:
            mvcount += 1
        else:
            bad_devices.append(device)

print(f"Total switches that meet standard: {mscount}")
print(f"Total APs that meet standard: {mrcount}")
print(f"Total Security Appliances that meet standard: {mxcount}")            
print(f"Total Cameras that meet standard: {mvcount}")
print(f"Devices that will need to be manually checked:")

for device in bad_devices:
    print("Serial#: " + device['serial'] + ", Model#:" + device['model'])