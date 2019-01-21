from mlask import MLAsk
import json, config
from requests_oauthlib import OAuth1Session

CK  = config.CONSUMER_KEY
CS  = config.CONSUMER_SECRET
AT  = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

params = {'count' : 10, "user_id" : "Rowing0914"}

res = twitter.get(url, params=params)

emotion_analyzer = MLAsk()

if res.status_code == 200:
	timelines = json.loads(res.text)
	for line in timelines:
		print(line['user']['name']+"::"+line['text'])
		result = emotion_analyzer.analyze(str(line['text']))
		print(result['emotion'])
		print(line['created_at'])
		print("======================================")
else:
	print("failed....")
