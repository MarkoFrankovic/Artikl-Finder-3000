from fastapi import FastAPI
import aiohttp
import asyncio
import pymongo

app = FastAPI()

#myclient = pymongo.MongoClient(
    #"mongodb+srv://Korisnik:korisnik@databaza.tip3k.mongodb.net/Databaza?retryWrites=true&w=majority")

myclient = pymongo.MongoClient(
    "mongodb+srv://Marko:marko39@databaza.hhhcb9p.mongodb.net/Databaza?retryWrites=true&w=majority")

#izbor databaze
mydb = myclient["Databaza"]

Artikli = mydb["Artikli"]

print(Artikli)

@app.route('/api/artikli', methods=['POST'])
def upis_u_bazu():
   data = request.get_json()
   print(json_util.dumps(data))
   mydict = data
   data["ocjena"] = int(data["ocjena"])
   Pjesme.insert_one(data)
   return data