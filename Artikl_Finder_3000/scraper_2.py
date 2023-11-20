import asyncio
from bs4 import *
import requests

def scraper():

    title = "Kaufland"
    url = "https://www.kaufland.hr/ponuda/ponuda-od-cetvrtka/ponuda-pregled.category=01_Meso__perad__kobasice.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    title = []
    subtitle = []

    for tag in soup.find_all("h4",{"class":"m-offer-tile__title"}):
        names = tag.text.strip()
        print(names)

    for tag in soup.find_all("h5",{"class":"m-offer-tile__subtitle"}):
        names = tag.text.strip()
        print(names)

    for tag in soup.find_all("div",{"class":"a-pricetag__price"})[::2]:
        price = tag.text.strip()[:-2].strip()
        #print(price)
    

scraper()