# UTCReading-Takeover

Please clone or download this repo to begin.

To start, please make sure you have python3 (important that its 3), git, Flask and the webex teams SDK (links below)

https://github.com/CiscoDevNet/webexteamssdk

https://github.com/pallets/flask

Now look in your chats, and you should see a token that is provided. If you have no token then contact someone from Cisco.

Once this is done, you can simply start by running the start.py file.

This file is designed for OSX or Linux, so if this file is crashing please do the following:

Set the following environment variables in python:

 - WEBEX_TEAMS_ACCESS_TOKEN to the token we will cover later
 
 - FLASK_APP to bot_server.py
 
 - paste your token with no spaces after or new lines after into a file called access.tkn
 
 - run the command "python -m flask run --host=0.0.0.0"
 
The above is the equivilant of running the file.

One the first time of running the file, you will be prompted for an access token, this can be found in your team chat.

You should now be able to talk to your bot by @mentioning it in your team chat.

Your bot is called the same as your team chat, so something like "Group x Team y".

Now have a look at the bot_server.py file and start to play.

Pretty much all of your editing should be in the function replyLogic.

The variables message and room have been passed into this function for you to use, but add more as you see fit.

message is a string that contains the users message, and room is a string that contains the room ID used to respond to.

Try changing the output depending on what the users input is.

If you are struggling, use Developer.webex.com Google and your mentors to help. 

If you are still really struggling, message Simon Light, but i will be slow replying.

Good Luck!


Put token in access.tkn

install dependecies

Set environment variables

run code
