from flask import Flask, request
from mlask import MLAsk
from requests_oauthlib import OAuth1Session
import json, config

app = Flask(__name__)

def tw_search(user_id):
	params = {'count' : 10, "user_id" : user_id}

	res = twitter.get(url, params=params)

	emotion_analyzer = MLAsk()

	if res.status_code == 200:
		result = {}
		for index, line in enumerate(json.loads(res.text)):
			temp = emotion_analyzer.analyze(str(line['text']))

			# create result
			if temp["emotion"] != None:
				result[str(index)] = {"message" : temp["text"], "emotion" : temp["emotion"], "intension" : temp["intension"], "orientation" : temp["orientation"]}
			else:
				result[str(index)] = {"message" : temp["text"], "emotion" : False, "intension" : False, "orientation" : False}

			# displaying the result on console
			print(line['user']['name']+"::"+line['text'])
			print(line['created_at'])
			print("======================================")

		return str(result)
	else:
		print("failed....")
		return "failed"

@app.route('/')
def index():
	return 'hello world'

@app.route('/input')
def input():
	return """
			<form method="POST" action="/search">
			  User id:<br>
			  <input type="text" name="user_id"><br>
			</form>
		   """

@app.route('/search', methods=['POST'])
def search():
	user_id = request.form['user_id']
	return tw_search(user_id)

if __name__ == '__main__':
	# loading configs
	CK  = config.CONSUMER_KEY
	CS  = config.CONSUMER_SECRET
	AT  = config.ACCESS_TOKEN
	ATS = config.ACCESS_TOKEN_SECRET
	twitter = OAuth1Session(CK, CS, AT, ATS)
	url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

	app.run(debug=True)