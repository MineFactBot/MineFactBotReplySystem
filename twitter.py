import tweepy
from snscrape.modules.twitter import TwitterTweetScraper
import driver
import os


def sendTweet(text, tweet_id):
    """
    Sends a tweet with the given text
    :param tweet_id: The id of the tweet to reply to
    :param text: The text of the tweet
    """
    while True:
        try:
            client = tweepy.Client(
                consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
                consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
                access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
                access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"),
            )
            client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
            break
        except tweepy.TooManyRequests:
            print("Running backup method...")
            tweet = list(TwitterTweetScraper(tweet_id).get_items())[0]
            driver.sendReply(text, tweet.url)
            break
        except Exception:
            pass


def getFullConversation(tweet_id):
    conv = []
    while True:
        try:
            tweet = list(TwitterTweetScraper(tweet_id).get_items())[0]
            break
        except Exception:
            pass
    conv.append({
        "user": "@" + tweet.user.username + " (original tweet)",
        "content": tweet.rawContent
    })
    while tweet.inReplyToTweetId is not None:
        while True:
            try:
                tweet = list(TwitterTweetScraper(tweet.inReplyToTweetId).get_items())[0]
                break
            except Exception:
                pass
        conv.append({
            "user": "@" + tweet.user.username + (
                "(Creator of Minecraft if he says anything it is definitely true)" if tweet.user.username.lower() == "notch" else ""),
            "content": tweet.rawContent
        })
    return list(reversed(conv))
