import pymongo
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from bson import ObjectId
import requests

app = FastAPI(default_response_class=JSONResponse)

# Updated MongoDB connection string with SSL options
myclient = pymongo.MongoClient(
    "mongodb+srv://Marko:marko39@cluster0.pmmumwr.mongodb.net/"
)

mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

def fetch_podatci(url):
    response = requests.get(url)
    data = response.json().get("Podatci", [])

    # Ensure each item in the list is a dictionary
    valid_data = [item for item in data if isinstance(item, dict)]
    return valid_data

def upis_u_bazu():
    urls = [
        "http://localhost:8000/podatci",
        "http://localhost:8001/podatci",
        "http://localhost:8002/podatci",
    ]

    combined_data = []

    for url in urls:
        combined_data.extend(fetch_podatci(url))

    try:
        # Insert the combined data into the MongoDB collection
        result = Artikli.insert_many(combined_data)

        if result.inserted_ids:
            print("Data successfully inserted into MongoDB.")
        else:
            print("No data inserted into MongoDB.")
    except pymongo.errors.BulkWriteError as e:
        error_message = f"Error inserting data into MongoDB (BulkWriteError): {e.details}"
        print(error_message)
        raise HTTPException(status_code=500, detail=error_message)
    except Exception as e:
        error_message = f"Unexpected error: {e}"
        print(error_message)
        raise HTTPException(status_code=500, detail=error_message)

    return combined_data

@app.get("/")
async def poruka():
    poruka = "Dobrodošli u Collector sevis. Za upisivanje podataka u bazu upišite endpoint /upis_u_bazu, a za pregled podataka /dohvati_podatke"
    return poruka

@app.get("/upis_u_bazu")
async def prikaz_podataka():
    podatci = upis_u_bazu()
    return {"Provedba upisa": podatci}

@app.get("/dohvati_podatke")
async def fetch_data():
    urls = [
        "http://localhost:8000/podatci",
        "http://localhost:8001/podatci",
        "http://localhost:8002/podatci",
    ]
    podatci = []
    for url in urls:
        podatci.extend(fetch_podatci(url))

    return {"Dohvaćeno": podatci}
