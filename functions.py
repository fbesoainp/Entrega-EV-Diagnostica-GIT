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
    pass



def topHashtags(data):
    pass