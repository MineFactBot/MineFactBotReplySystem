# Minecraft Facts Twitter Bot - Reply System

This is the source code for the reply system of the Minecraft Facts Twitter Bot. The goal of this system is to allow the bot to reply to tweets that mention it and reply to it, providing users with more information about Minecraft.

## Technologies

This system is built with Python and uses the Tweepy and snscrape libraries to interact with the Twitter API. It also uses OpenAI's GPT-3.5 to generate answers

## Setup

To run this system, you will need to set up a few things:

1. Create a Twitter account for the bot and obtain API keys and access tokens.
2. Install the required Python libraries (Tweepy and OpenAI).
3. Set up a GPT-3.5 API key and configure the OpenAI library.

Once you have done these things, you can clone this repository and run the `main.py` file to start the reply system.

## How it works

The reply system listens for mentions of the bot's Twitter handle (`@minefactbot`). When it detects a mention or reply, it uses the snscrape library to retrieve the text of the tweet and the user who sent it.

The system then passes the text of the tweet to the OpenAI GPT-3.5 model, which generates an answer. The answer is then tweeted as a reply to the original tweet, tagging the user who sent it.

## Improvements

This system can be improved in a few ways:

1. Smarter fact generation: The OpenAI GPT-3.5 model is quite good at generating Minecraft facts, but there is still room for improvement. The system could be improved by using a more powerful model or by training a custom model on Minecraft-specific data.
2. More interaction: Currently, the system only replies to mentions of the bot's Twitter handle. It could be improved to listen for other types of interactions, such as direct messages or mentions of specific keywords.

## Conclusion

The Minecraft Facts Twitter Bot's reply system is a simple but effective way to provide users with more information about Minecraft. While there is room for improvement, the system currently works well and is a useful tool for Minecraft fans on Twitter.
