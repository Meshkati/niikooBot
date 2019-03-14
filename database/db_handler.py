"""
    This module provides all of the stuffs about handling the data with database
    There is no other models or something for managing data, everything is here :(
"""
import pymongo

# Setups the connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_name = "niikoo"


# Creates collections if necessary
def get_collection(collection_name):
    db = mongo_client[db_name]
    return db[collection_name]


# Inserts a generated code to user
def insert_code(user, code):
    users = get_collection("users")
    # creating the item
    item = {"user_id": user.id, "code": code}
    # inserts into collection
    result = users.insert_one(item)

    return result.inserted_id


# Gets the invite code of a user
def get_code(user):
    users = get_collection("users")
    result = users.find_one({"user_id": user.id})
    print(result)

    if result is None:
        return None

    return result["code"]
