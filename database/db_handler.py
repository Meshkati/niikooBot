"""
    This module provides all of the stuffs about handling the data with database
    There is no other models or something for managing data, everything is here :(
"""
import pymongo

# Setups the connection
mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db_name = "niikoo"


# FIXME: Change the users to user_ids

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


# Insert the code of a user into another user
def add_code(user, code):
    users = get_collection("users")
    found_user = users.find_one({"code": code})
    if found_user is None:
        return None

    result = users.update_one({"user_id": user.id}, {"$push": {"network": found_user["user_id"]}})
    if result is None:
        return None
    # FIXME: Move this part into the logic of add_code_handler
    result = users.update_one({"user_id": found_user["user_id"]}, {"$push": {"network": user.id}})

    return result


# Adds an amount of credit to a user, or if it hasn't any credits yet, initializes it
def add_credit(user_id, credit):
    users = get_collection("users")
    user = users.find_one({"user_id": user_id})
    last_credit = 0
    if "credit" in user:
        last_credit = user["credit"]

    result = users.update_one({"user_id": user_id}, {"$set": {"credit": credit + last_credit}})

    return result


# Gets the credit of a user
def get_credit(user_id):
    users = get_collection("users")
    user = users.find_one({"user_id": user_id})
    if user is None:
        return 0

    return user["credit"]
