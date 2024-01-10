import asyncio
from fastapi import FastAPI
import pymongo

app = FastAPI()

myclient = pymongo.MongoClient(
    "mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")

mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]


def finder():

    #x = Artikli.find({ "name": ime_artikla },{ "_id": 1, "name": 1, "price": 1 , "tittle": 1})
    #ime_artikla = input("Upisite ime željenog artikla: ")

    for x in Artikli.find({},{ "_id": 0, "name": 1, "price": 1 , "title": 1}):
        print(x)

        a = x.get("name")

    print(a)

    #print(Svi_Artikli)
    #return Svi_Artikli
    return x

finder()
