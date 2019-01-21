from urllib import request
import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

def line_send(message):
	token = "prSv6xk3bI6kGAqcxRRyKempL6kQVuTvIDYhSg8gU0Z"
	url = 'https://notify-api.line.me/api/notify'
	headers = {"Authorization": "Bearer " + token}
	payload = {"message": message}

	r = requests.post(url, headers=headers, params=payload)
	return r

def scraping():
	#url
	url = "http://www.yomiuri.co.jp/"

	#get html
	html = request.urlopen(url)

	#set BueatifulSoup
	soup = BeautifulSoup(html, "html.parser")

	#get headlines
	mainNewsIndex = soup.find("ul", attrs={"class", "list-main-news"})
	headlines = mainNewsIndex.find_all("span", attrs={"class", "headline"})

	result = []

	#print headlines
	for headline in headlines:
		result.append(headline.contents[0]+headline.span.string+"\n")

	return line_send(result)

@app.route('/')
def hello():
	print(scraping())
	return "nam"

@app.route('/good')
def good():
	name = "Good"
	return name

## おまじない
if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)