# UTCReading-Takeover

## Installing dependencies

Please clone or download this repo to begin.

To start, please make sure you have python, Flask and the webex teams SDK (links below)

https://github.com/CiscoDevNet/webexteamssdk

https://github.com/pallets/flask

## Setting up environment

Now look in your chats, and you should see a token that is provided. If you have no token then contact someone from Cisco.

Place this token in a new file called access.tkn.

Make sure there are no spaces or new lines in this file or it wont work

Now we need to set environment variables.

If you dont know how to do this please use google, it is a fairly simple process.

On Linux/OSX you use the export command.

In windows you will need to do this through settings.

Set the following environment variables:

 - WEBEX_TEAMS_ACCESS_TOKEN to the token that you had in chat.
 
 - FLASK_APP to bot_server.py
 
That is the environment setup.

## Running the server

To start the server you need to run the command "python -m flask run --host=0.0.0.0"
 
You should now be able to talk to your bot by @mentioning it in your team chat.

Your bot is called the same as your team chat, so something like "Group x Team y".

## Next steps

Now have a look at the bot_server.py file and start to play.

Pretty much all of your editing should be in the function replyLogic.

The variables message and room have been passed into this function for you to use, but add more as you see fit.

message is a string that contains the users message, and room is a string that contains the room ID used to respond to.

Try changing the output depending on what the users input is.

If you are struggling, use Developer.webex.com Google and your mentors to help. 

If you are still really struggling, message Simon Light, but i will be slow replying.

Good Luck!
