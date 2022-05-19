# GOAL: Get title of every book with a 2 star rating

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format(1))

soup = bs4.BeautifulSoup(res.text,'lxml')

products = soup.select(".product_pod")

example = products[0]

print("star-rating Three" in str(example))
