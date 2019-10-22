import socket
import time
import requests
import json
from flask import Flask
from flask import request
from webexteamssdk import WebexTeamsAPI, Webhook

def replyLogic(message, room):
    api.messages.create(room.id, text=str("Hello! This is how you reply to a message"))
    # this is where all your logic goes. Fell free to edit any of the code, but this is where the main logic resides
    return OK


api = WebexTeamsAPI()
f = open('./access.tkn', 'r')
bot_token = f.read()
f.close()

# Find all rooms that have 'webexteamssdk Demo' in their title
all_rooms = api.rooms.list()
demo_room = [room for room in all_rooms if 'webexteamssdk Demo' in room.title]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def messageHandling():
    json_data = request.data
    # Create a Webhook object from the JSON data
    webhook_obj = Webhook(json_data)
    # Get the room details
    room = api.rooms.get(webhook_obj.data.roomId)
    # Get the message details ATM messages.get is bad, and i think it has delay while getting group chat messages
    try:
        message = api.messages.get(webhook_obj.data.id)
    except:
        print("Message couldnt be read!")
        exit()
    # Get the sender's details
    person = api.people.get(message.personId)
    me = api.people.me()

    print("NEW MESSAGE IN ROOM '{}'".format(room.title))
    print("FROM '{}'".format(person.displayName))
    print("MESSAGE '{}'\n".format(message.text))

    if message.personId == me.id:
        return 'OK'
    else:
        replyLogic(message.text, room)
    return 'OK'


