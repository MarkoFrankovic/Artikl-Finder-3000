from fastapi import FastAPI
import asyncio
import pymongo
import requests
import bson.json_util as json_util
import os
from bson.objectid import ObjectId

app = FastAPI()

#mongodb+srv://Marko:<password>@cluster0.byoifdj.mongodb.net/

myclient = pymongo.MongoClient(
    "mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")

#izbor databaze
mydb = myclient["Databaza"]

Artikli = mydb["Artikli"]

def upis_u_bazu():
   response = requests.get(f"http://localhost:8000/podatci")
   rezultat = response.json()
   mydict = rezultat
   Artikli.insert_many(mydict["Podatci"])
   return rezultat

upis_u_bazu()