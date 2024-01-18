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

   #links=["http://localhost:8000/podatci","http://localhost:8001/podatci","http://localhost:8002/podatci"]
   #for url in links:
      #response = requests.get(url)

   #mydict = rezultat

   rezultat = response.json()
   rezultat2 = response2.json()
   rezultat3 = response3.json()

   print(rezultat2)

   lista = list(rezultat)
   lista2 = list(rezultat2)
   lista3 = list(rezultat3)

   sve_skupa = lista + lista2 + lista3

   print(sve_skupa)

   #Artikli.insert_many(mydict["Podatci"])
   return lista

upis_u_bazu()