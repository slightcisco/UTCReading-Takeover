# UTCReading-Takeover

To start off with, go to developer.webex.com and create an account.

Once there, click documentation, API reference and then messages.

Here is a list of all the things you can do with messages (list, create, delete).

Now click List messages.

We are now shown a path (/v1/messages) and a method (GET) in the center of the screen, as well as a series of headers and parameters on the right.

One of those Headers is a Bearer token.

I have posted the Bearer tokens in each of your group chats alread.

These correspond with the bots in your chat (that have the same name as your chat).

We can now use a HTTP GET request (in any programming language), passing the headers and parmaters listed on the page to receive a response of messages recieved.

Along with each of these messages we get back, we also get much more information that is listed at the bottom of the screen.

We could use this to check if a message has been sent in the last second, as this may be one our bot needs to reply to.

Use the rest of the documentation from developer.webex.com as well as Google to help create a bot that will help your classroom of the future.

GOOD LUCK
