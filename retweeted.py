import json

data = [json.loads(line) for line in open("farmers-protest-tweets-2021-03-5.json", "r", encoding="utf-8")]

def top_10_retweet(data):
    return sorted(data, key=lambda k: k["retweetCount"], reverse=True)[:10]