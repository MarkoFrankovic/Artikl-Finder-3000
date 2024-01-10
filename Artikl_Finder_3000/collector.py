from fastapi import FastAPI
import pymongo
import httpx

app = FastAPI()

myclient = pymongo.MongoClient("mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")
mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

@app.on_event("shutdown")
def shutdown_event():
    myclient.close()

async def upis_u_bazu():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8000/podatci")
        rezultat = response.json()
        mydict = rezultat
        Artikli.insert_many(mydict["Podatci"])
        return rezultat

upis_u_bazu()