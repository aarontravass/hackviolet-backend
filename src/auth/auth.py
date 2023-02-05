from src.database.mongodb.config import Mongo

instance = Mongo()
instanceDB = instance.get_db()
users_collection = instanceDB['users']

def addUser(body) -> dict:
    response = {}
    mongo_res = users_collection.find({'email':body.get('email')})


if __name__ == "__main__":
    instance = Mongo()
    usersDB = instance.get_users()
