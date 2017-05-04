import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
	url = 'http://www.cpubenchmark.net/high_end_cpus.html'
	source_code = requests.get(url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text)
	for link in soup.findAll('td', {'class': 'chart'}):
		href = link.get('href')
		inside = link.string
		print(inside)

trade_spider(1)