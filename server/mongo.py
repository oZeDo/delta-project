from pymongo import MongoClient
db = MongoClient('95.213.37.13')


def return_mongo(collection, id_):
    return db.bot[collection].distinct(id_)


def find_emote_id(name):
    return str(db.bot.emotes.find_one({"Name": name})['id'])












