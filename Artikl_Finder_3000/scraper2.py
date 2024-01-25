import asyncio
from bs4 import BeautifulSoup
import requests
from fastapi import FastAPI

app = FastAPI()

def Scraper():
    title = "Kaufland"
    subtitle = []
    price_list = []

    url = "https://www.kaufland.hr/ponuda/ponuda-od-cetvrtka/ponuda-pregled.category=01_Meso__perad__kobasice.html"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    title_data = soup.find("h1", {"class": "a-heading__title"})
    if title_data:
        title = title_data.text.strip()

    for tag in soup.find_all("h4", {"class": "m-offer-tile__title"}):
        names = tag.text.strip()
        subtitle.append(names)

    for tag in soup.find_all("div", {"class": "a-pricetag__price"})[::2]:
        price = tag.text.strip()[:-2].strip()
        price_list.append(price)

    # Combine title, subtitle, and price into a list of dictionaries
    combined_data = [
        {"name": f"{title} - {s}", "price": p, "title": title}
        for s, p in zip(subtitle, price_list)
    ]

    return combined_data

@app.get("/podatci")
async def prikaz_podataka():
    podatci = Scraper()
    return {"Podatci": podatci}
