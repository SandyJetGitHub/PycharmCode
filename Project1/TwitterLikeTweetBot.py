import tweepy

auth = tweepy.OAuthHandler('m9DeR9Yo3X6xdJ7hvslfsftqf', 'xyXFGVcHWaTn2MWH9tCvMQHhIcvKBqTWWcbTj6vv6KWVHOkK9q')
auth.set_access_token('166173157-4TejjI47xTvfTFlIPIxD5rbftS30SAQCDy3Yb8BI',
                      'awLuc0uY6Ny8pXMfq5cjUiSElp4Kb7CqTAo1c5C6Sb90U')

api = tweepy.API(auth)
search_string = '#Dream11IPL'
number_of_search = 2

for tweet in tweepy.Cursor(api.search, search_string).items(number_of_search):
    try:
        tweet.favorite()
        print('I liked the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
