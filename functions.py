import operator
import re

def topTweets(data):
    data.sort(key=operator.itemgetter('retweetCount'), reverse=True)
    return data[:10]

def topUsers(data):
    users = []
    ids = []

    for tweet in data:
        if tweet['user']['id'] not in ids:
            users.append(tweet['user'])
            ids.append(tweet['user']['id'])

    users.sort(key=operator.itemgetter('statusesCount'), reverse=True)
    return users[:10]

def topDays(data):
    days = []
    for tweet in data:
        day = tweet['date'].split("T")[0]
        days.append(day)
    days = [[x,days.count(x)] for x in set(days)]
    days.sort(key=lambda x: x[1], reverse=True)
    return days[:10]


def topHashtags(data):
    hashtags = []
    for tweet in data:
        tweetHashtags = re.findall(r"#(\w+)", tweet['content'])
        for hashtag in tweetHashtags:
            hashtags.append(hashtag)
    hashtags = [[x,hashtags.count(x)] for x in set(hashtags)]
    hashtags.sort(key=lambda x: x[1], reverse=True)
    return hashtags[:10]