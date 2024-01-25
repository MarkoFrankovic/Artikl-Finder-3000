from fastapi import FastAPI
import pymongo
import requests
import json

app = FastAPI()

myclient = pymongo.MongoClient("mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")
mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

def upis_u_bazu():
    response = requests.get(f"http://localhost:8000/podatci")
    response2 = requests.get(f"http://localhost:8001/podatci")
    response3 = requests.get(f"http://localhost:8002/podatci")

    rezultat = response.json()
    rezultat2 = response2.json()
    rezultat3 = response3.json()

    print(rezultat)
    print(rezultat2)
    print(rezultat3)

    # Combine the JSON responses into one list
    combined_data = rezultat["Podatci"] + rezultat2["Podatci"] + rezultat3["Podatci"]

    print(combined_data)

    # Insert the combined data into the MongoDB collection
    #Artikli.insert_many(combined_data)

    return combined_data

upis_u_bazu()
