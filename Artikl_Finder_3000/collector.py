from fastapi import FastAPI
import pymongo
import requests

app = FastAPI()

myclient = pymongo.MongoClient("mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")
mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

def upis_u_bazu():
   response = requests.get(f"http://localhost:8000/podatci")
   rezultat = response.json()
   mydict = rezultat
   Artikli.insert_many(mydict["Podatci"])
   return rezultat

upis_u_bazu()