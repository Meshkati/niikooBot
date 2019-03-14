"""
    This module provides all of the stuffs about handling the data with database
    There is no other models or something for managing data, everything is here :(
"""
import pymongo

# Setups the connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_name = "niikoo"


# Creates collections if necessary
def migrate():
    db = mongo_client[db_name]
    users = db["users"]


# Inserts a generated code to user
def insert_code(user, code):
    db = mongo_client[db_name]
    users = db["users"]
    # creating the item
    item = {"user_id": user.id, "code": code}
    # inserts into collection
    result = users.insert_one(item)

    return result.inserted_id
