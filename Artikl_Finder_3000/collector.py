from fastapi import FastAPI
import pymongo
import requests

app = FastAPI()

myclient = pymongo.MongoClient("mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")
mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

def fetch_podatci(url):
    response = requests.get(url)
    return response.json().get("Podatci", [])

def upis_u_bazu():
    urls = [
        "http://localhost:8000/podatci",
        "http://localhost:8001/podatci",
        "http://localhost:8002/podatci",
    ]

    combined_data = []
    for url in urls:
        combined_data.extend(fetch_podatci(url))

    # Print the combined data
    print(combined_data)

    # Insert the combined data into the MongoDB collection
    # Artikli.insert_many(combined_data)

    return combined_data

upis_u_bazu()
