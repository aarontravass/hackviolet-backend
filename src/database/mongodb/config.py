import os
from typing import Any, Mapping

from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.database import Database

load_dotenv()


class Mongo:
    def __int__(self):
        self.CONNECTION_STRING = os.getenv('MONGODB_URI')
        self.client = MongoClient(self.CONNECTION_STRING)

    def get_db(self) -> Database[Mapping[str, Any] | Any]:
        return self.client['public']
