from urllib import request
import requests
from bs4 import BeautifulSoup

def line_send(token, message):
	token = token
	url = 'https://notify-api.line.me/api/notify'
	headers = {"Authorization": "Bearer " + token}
	payload = {"message": message}

	r = requests.post(url, headers=headers, params=payload)
	return r

def scraping(token):
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

	return line_send(token, result)

if __name__ == '__main__':
	token = input("give me your token!!\n")
	# token = "prSv6xk3bI6kGAqcxRRyKempL6kQVuTvIDYhSg8gU0Z"
	print(scraping(token))
	# message = "Hello World!!"
	# print(line_send(message))