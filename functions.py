import operator

def topTweets(data):
    data.sort(key=operator.itemgetter('retweetCount'), reverse=True)
    return data[:10]


def topUsers(data):
    pass

def topDays(data):
    pass 

def topHashtags(data):
    pass