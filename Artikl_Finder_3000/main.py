import asyncio
from fastapi import FastAPI
import pymongo

app = FastAPI()

myclient = pymongo.MongoClient(
    "mongodb+srv://Marko:marko39@cluster0.byoifdj.mongodb.net/")

mydb = myclient["Databaza"]
Artikli = mydb["Artikli"]

def convert_price_to_int(price_str):
    # Remove any non-digit characters from the price string and convert to integer
    return int(''.join(filter(str.isdigit, price_str)))

def show_all_items():
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    items = Artikli.find({}, projection)
    print("All items:")
    for item in items:
        item["price"] = convert_price_to_int(item["price"])
        print(item)

def show_items_in_title(title):
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    query = {"title": {"$regex": f".*{title}.*", "$options": "i"}}
    items = Artikli.find(query, projection)
    print(f"All items in title '{title}':")
    for item in items:
        item["price"] = convert_price_to_int(item["price"])
        print(item)

def show_items_by_price(sort_order):
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    items = Artikli.find({}, projection).sort("price", sort_order)
    print(f"All items sorted by price ({sort_order}):")
    for item in items:
        item["price"] = convert_price_to_int(item["price"])
        print(item)

def show_items_in_title_by_price(title, sort_order):
    projection = {"_id": 0, "name": 1, "price": 1, "title": 1}
    query = {"title": {"$regex": f".*{title}.*", "$options": "i"}}
    items = Artikli.find(query, projection).sort("price", sort_order)
    print(f"All items in title '{title}' sorted by price ({sort_order}):")
    for item in items:
        item["price"] = convert_price_to_int(item["price"])
        print(item)

def menu():
    while True:
        print("Choose an option:")
        print("1. Show all items")
        print("2. Show all items in a title")
        print("3. Show all items sorted by price")
        print("4. Show items in a title sorted by price")
        print("5. End")

        option = input("Enter your choice (1-5): ")

        if option == "1":
            show_all_items()
        elif option == "2":
            title = input("Enter the title: ")
            show_items_in_title(title)
        elif option == "3":
            sort_order = input("Enter the sorting order (ASC or DESC): ").upper()
            show_items_by_price(sort_order)
        elif option == "4":
            title = input("Enter the title: ")
            sort_order = input("Enter the sorting order (ASC or DESC): ").upper()
            show_items_in_title_by_price(title, sort_order)
        elif option == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option")

# Example usage:
menu()
