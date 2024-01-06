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
    #x = Artikli.find({ "name": ime_artikla },{ "_id": 1, "name": 1, "price": 1 , "tittle": 1})
    #print(x)
    #for x in Artikli.find({ "name": ime_artikla },{ "_id": 1, "name": 1, "price": 1 , "tittle": 1}):
        #print(x)


    for x in Artikli.find({ "_id": 1, "name": 1, "price": 1 , "tittle": 1}):
        print(x)

    #ime_artikla = input("Upisite ime željenog artikla: ")

    #y = print(x.get("name": ime_artikla))

finder()


#Ispis svih artikala
#option = { "_id": 1, "name": 1, "price": 1 , "tittle": 1}
    #for x in Artikli.find(option):
        #print(x)