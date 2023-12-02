import asyncio
from bs4 import *
import requests
from fastapi import FastAPI

def scraper():

    title = "Kaufland"
    url = "https://www.kaufland.hr/ponuda/ponuda-od-cetvrtka/ponuda-pregled.category=01_Meso__perad__kobasice.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    title = []
    subtitle = []
    full_name = title + subtitle

    for tag in soup.find_all("h4",{"class":"m-offer-tile__title"}):
        names = tag.text.strip()
        
    title.append(names)
    print(title)

    for tag in soup.find_all("h5",{"class":"m-offer-tile__subtitle"}):
        names = tag.text.strip()
    
    subtitle.append(names)
    print(subtitle)   

    for tag in soup.find_all("div",{"class":"a-pricetag__price"})[::2]:
        price = tag.text.strip()[:-2].strip()
        print(price)
    

scraper()