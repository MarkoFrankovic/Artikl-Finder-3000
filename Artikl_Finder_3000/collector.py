from fastapi import FastAPI
import pymongo
import requests

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

   rezultat = response.json() 
   rezultat2 = response2.json()  
   rezultat3 = response3.son()
   print(rezultat2)
   mydict = rezultat
   #Artikli.insert_many(mydict["Podatci"])
   return rezultat


   

upis_u_bazu()