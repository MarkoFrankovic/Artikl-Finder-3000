import asyncio
from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI

app = FastAPI()

def Scraper():
    title = "Konzum"
    url = "https://www.konzum.hr/web/posebne-ponude?sort%5B%5D=&per_page=100"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    for tag in soup.find_all("div", {"data-ga-type": "productImpression"}):
        names = tag.attrs["data-ga-name"]
        price = tag.attrs["data-ga-price"][:-2]
        data.append({"name": names, "price": price, "title": title})

    return data

@app.get("/podatci")
async def prikaz_podataka():
    podatci = Scraper()
    return {"Podatci": podatci}
