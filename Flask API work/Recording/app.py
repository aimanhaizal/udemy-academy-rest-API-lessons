from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]

# Use this decorator for Flask 2.x
@app.get("/store")

#this creates a flask app

#lesson 55, REST api endpoint

def get_stores():
    return {"stores": stores}

# if __name__ == "__main__":
#     app.run(debug=True)

#lecture 56, what is json
#a long string with lists, booleans, and such

#lesson 57, interacting with our REST api
#making with insomnia

#lesson 58, creating stores in the REST api
@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201

#lesson 59: creating items in each store
@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()#this grabs the incoming json file
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found!"}, 404
    

#lesson 60: how to get specific store and its items
# Getting a specific store (GET)
@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found!"}, 404

@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found!"}, 404