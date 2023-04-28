import os
import sys
import time

from snscrape.modules.twitter import TwitterSearchScraper, TwitterTweetScraper
import ai
import twitter
from dotenv import load_dotenv
load_dotenv()


def countdown(t, step=1, msg='sleeping'):  # in seconds
    """
    Counts down from t to 0
    :param t: The time to count down from
    :param step: The step to count down
    :param msg: The message to print
    """
    pad_str = ' ' * len('%d' % step)
    for i in range(t, 0, -step):
        print(f'\r{msg.capitalize()} for the next {i} seconds {pad_str}', end='')
        sys.stdout.flush()
        time.sleep(step)
    print(f'Done {msg} for {t} seconds!  {pad_str}')
    print("\n\n\n\n\n\n\n")


with open("lastid", "r") as f:
    last_tweet = int(f.read())
while True:
    while True:
        try:
            tweets = list(TwitterSearchScraper(query=f"to:minefactbot since_id:{last_tweet}").get_items())
            break
        except Exception:
            pass
    for i, tweet in enumerate(list(reversed(tweets))):
        print("Tweet received " + tweet.url)
        notfound = False
        if tweet.inReplyToUser is not None:
            while True:
                try:
                    inReplyToTweet = list(TwitterTweetScraper(tweet.inReplyToTweetId).get_items())[0]
                    break
                except IndexError:
                    print("Tweet not found")
                    notfound = True
                    break
                except Exception as e:
                    print(e)
                    pass
            if notfound:
                continue
            reply = ai.generateAnswer(twitter.getFullConversation(tweet.id), True)
        else:
            reply = ai.generateAnswer(twitter.getFullConversation(tweet.id), False)
        twitter.sendTweet(reply, tweet.id)
        last_tweet = tweet.id
        print("Tweet sent")
        with open("lastid", "w") as f:
            f.write(str(last_tweet))
    countdown(200)
