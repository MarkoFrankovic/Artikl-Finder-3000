import asyncio
from bs4 import *
import requests

def scraper():

    title = "Konzum"
    url = "https://www.konzum.hr/web/posebne-ponude?sort%5B%5D=&per_page=100"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all("div",{"data-ga-type":"productImpression"}):
        names = tag.attrs["data-ga-name"]
        price = tag.attrs["data-ga-price"][:-2]
        print(names,price)

scraper()