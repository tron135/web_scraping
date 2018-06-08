import requests
from bs4 import BeautifulSoup
from time import sleep
from csv import writer
import io

all_quotes = []
base_url = "http://quotes.toscrape.com"
url = "/page/1"

with open("quote_data.csv", "a", encoding="utf-8") as csv_file:
	csv_writer = writer(csv_file)
	csv_writer.writerow(["Quote", "Author", "Bio-Link"])

	while url:
		res = requests.get(f"{base_url}{url}")
		print(f"Now Scraping {base_url}{url}....")
		soup = BeautifulSoup(res.text, "html.parser")
		quotes = soup.find_all(class_="quote")
		
		for quote in quotes:
			text = quote.find(class_="text").get_text()
			author = quote.find(class_="author").get_text()
			biolink = quote.find("a")["href"]
			csv_writer.writerow([text, author, biolink])

		nxt_btn = soup.find(class_="next")
		url = nxt_btn.find("a")["href"] if nxt_btn	else None
		# sleep(2)

	# print(all_quotes)