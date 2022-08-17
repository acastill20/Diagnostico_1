import json
import retweeted

data = [json.loads(line) for line in open("farmers-protest-tweets-2021-03-5.json", "r", encoding="utf-8")]

def main(accion):

    if accion == "top_10_retweet":
        return retweeted.top_10_retweet(data)
