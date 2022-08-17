def top_10_retweet(data):
    return sorted(data, key=lambda k: k["retweetCount"], reverse=True)[:10]