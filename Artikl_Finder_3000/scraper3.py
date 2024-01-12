import asyncio
from bs4 import *
import requests
from fastapi import FastAPI

app = FastAPI()

def scraper():

    title = "Tommy"
    url = "https://www.tommy.hr/akcije"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup.find_all("h3",{"class":"mb-2 text-sm pr-2 font-normal text-gray-900 line-clamp-2 hover:underline cursor-pointer"}):
        names = tag.text.strip()
        print(names)

    for tag in soup.find_all("span",{"class":"mt-auto inline-block-block text-sm font-bold text-gray-900"})[::2]:
        price = tag.text.strip()[:-9].strip()
        print(price)

@app.get("/podatci")
async def prikaz_podataka():
    podatci = Scraper()
    return {"Podatci": podatci}