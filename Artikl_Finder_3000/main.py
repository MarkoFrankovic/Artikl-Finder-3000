import asyncio
from fastapi import FastAPI
import pymongo

app = FastAPI()

myclient = pymongo.MongoClient(
    "mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")

mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

#artikl = input("Koji artikl želite pronači?")

def finder():
    Svi_Artikli = Artikli.find_one()
    print(Svi_Artikli)
    return Svi_Artikli


finder()

