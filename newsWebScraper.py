import requests
from bs4 import BeautifulSoup
import json

def scrape(response_text):
    sp = BeautifulSoup (response_text, 'lxml')
    headlines = sp.find_all("h2", class_="title")
    for headline in headlines:
        print(headline.text)

url = 'https://www.npr.org/sections/news/'
response = requests.get(url)
scrape(response.text)




