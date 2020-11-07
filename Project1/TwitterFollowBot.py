import tweepy
import time

auth = tweepy.OAuthHandler('m9DeR9Yo3X6xdJ7hvslfsftqf', 'xyXFGVcHWaTn2MWH9tCvMQHhIcvKBqTWWcbTj6vv6KWVHOkK9q')
auth.set_access_token('166173157-4TejjI47xTvfTFlIPIxD5rbftS30SAQCDy3Yb8BI',
                      'awLuc0uY6Ny8pXMfq5cjUiSElp4Kb7CqTAo1c5C6Sb90U')

api = tweepy.API(auth)


# the below function used to limit the number of times hitting to twitter API
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# Need to wrap the for loop if number of follower are in hundreds and thousands
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)
    if follower.name == 'tejas gujarathi':
        follower.follow()

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#   print(tweet.text)

# user = api.me()
# print(user.name)
# print(user.screen_name)
# print(user.followers_count)
