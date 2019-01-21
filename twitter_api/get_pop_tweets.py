import json, config
from requests_oauthlib import OAuth1Session

CK  = config.CONSUMER_KEY
CS  = config.CONSUMER_SECRET
AT  = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/search/tweets.json"

params = {'q' : "royalholloway"}

res = twitter.get(url, params=params)

if res.status_code == 200:
	timelines = json.loads(res.text)
	print(timelines)
else:
	print("failed....")