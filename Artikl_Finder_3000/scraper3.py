import asyncio
from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI

app = FastAPI()

def Scraper():
    title = "Tommy"
    url = "https://www.tommy.hr/akcije"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    data = []

    name_tags = soup.find_all("h3", {"class": "mb-2 text-sm pr-2 font-normal text-gray-900 line-clamp-2 hover:underline cursor-pointer"})
    price_tags = soup.find_all("span", {"class": "mt-auto inline-block-block text-sm font-bold text-gray-900"})[::2]

    for name_tag, price_tag in zip(name_tags, price_tags):
        name = name_tag.text.strip()
        price = price_tag.text.strip()[:-1].strip()

        data.append({"name": name, "price": price, "title": title})
        print(name, price)

    return data

@app.get("/podatci")
async def prikaz_podataka():
    podatci = Scraper()
    return {"Podatci": podatci}
