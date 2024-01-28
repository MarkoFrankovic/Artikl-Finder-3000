import pymongo
from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
import requests

app = FastAPI()

myclient = pymongo.MongoClient("mongodb+srv://Marko:marko39@cluster0.pmmumwr.mongodb.net/")

mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

def convert_price_to_float(price_str):
    # Remove any non-digit characters from the price string and convert to float
    price = float(''.join(filter(lambda x: x.isdigit() or x in {',', '.'}, price_str.replace(',', '.'))))
    # Format the price with Euro symbol
    return f"{price:.2f} €"

def show_all_items(sort_option: str = Query(None, description="Sort by price or name (price or name)"),
                   sort_order: str = Query(None, description="Sorting order (ASC or DESC)")):
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    items = Artikli.find({}, projection)

    if sort_option and sort_order:
        sort_key = "price" if sort_option == "price" else "name"
        items = items.sort([(sort_key, pymongo.ASCENDING if sort_order == "ASC" else pymongo.DESCENDING)])

    result = []
    for item in items:
        item["price"] = convert_price_to_float(item["price"])
        result.append(item)

    return {"message": "All items", "data": result}

def show_items_in_title(title: str,
                        sort_option: str = Query(None, description="Sort by price or name (price or name)"),
                        sort_order: str = Query(None, description="Sorting order (ASC or DESC)")):
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    query = {"title": {"$regex": f".*{title}.*", "$options": "i"}}
    items = Artikli.find(query, projection)

    if sort_option and sort_order:
        sort_key = "price" if sort_option == "price" else "name"
        items = items.sort([(sort_key, pymongo.ASCENDING if sort_order == "ASC" else pymongo.DESCENDING)])

    result = []
    for item in items:
        item["price"] = convert_price_to_float(item["price"])
        result.append(item)

    return {"message": f"All items in title '{title}'", "data": result}

def search_specific_item(name: str):
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    query = {"name": {"$regex": f".*{name}.*", "$options": "i"}}
    item = Artikli.find_one(query, projection)

    if item:
        item["price"] = convert_price_to_float(item["price"])
        return {"message": "Specific item", "data": item}
    else:
        return {"message": f"No item found with the name '{name}'"}

# Trigger the upis_u_bazu logic when accessing the root endpoint
@app.get("/")
def read_root():
    # Call the /upis_u_bazu endpoint and print the returned message
    response = requests.get("http://127.0.0.1:8003/upis_u_bazu")
    result = response.json()
    poruka = "Dobrodošli u Menu servis. Za odabir opcija upišite endpoint /menu/ te broj opcije: 1. Prikaz svih artikala , 2. Prikaz artikala iz odabrane trgovine , 3. Prikaz artikla po nazivu , 4. Izlaz iz Menua"
    print(result["message"])
    return {"message": poruka}

@app.get("/menu/{option}")
def menu(option: int):
    if option == 1:
        return show_all_items()
    elif option == 2:
        title = input("Enter the title: ")
        return show_items_in_title(title)
    elif option == 3:
        name = input("Enter the name of the item: ")
        return search_specific_item(name)
    elif option == 4:
        # Redirect to the root endpoint when option 4 is selected
        return RedirectResponse(url="/", status_code=303)
    else:
        return {"message": "Invalid option"}

# To run the FastAPI app, use:
# uvicorn your_file_name:app --reload
