import subprocess
import json
import os
import requests
from time import sleep

def bashCommand(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return output

print("CHECKING DEPENDENCIES INSTALLED")
pip_list = bashCommand("pip list")
if "Flask" not in pip_list:
    print("Flask is not installed, please install to continue ")
    quit()
if "webexteamssdk" not in pip_list:
    print("Webex Teams SDK is not installed, please install to continue ")
    quit()
print ("Dependencies all installed")
try:
    f = open('./access.tkn', 'r')
    token = f.read()
    token_empty = False
    print("TOKEN FOUND IN access.tkn")
    f.close()
except :
    token_empty = True
    token = ""
    f = open('./access.tkn', 'w')
    print("No token was found")
print("Navigate to developer.webex.com and create an account/login")
print("Click your profile in the top right, click 'My Webex Teams Apps' and create a new bot")

while token_empty:
    token = raw_input("Please enter the ACCESS_TOKEN for your bot: ")
    if token == "":
        print("Please enter a token, cannot leave this blank")
    else:
        f.write(token)
        token_empty = False

os.environ['WEBEX_TEAMS_ACCESS_TOKEN'] = token
os.environ['FLASK_APP'] = "bot_server.py"
bashCommand("python -m flask run --host=0.0.0.0")

