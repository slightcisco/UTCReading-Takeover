# UTCReading-Takeover
Used for file storage on UTCR Take over day

To start, please make sure you have python, git, Flask and the webex teams SDK (links below)

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

Now have a look att the bot_server.py file and start to play
