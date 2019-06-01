_author_ = 'Ta-Seen Junaid'

import  pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(colllection, data):
        Database.DATABASE[colllection].insert(data)


    @staticmethod
    def find(colllection, query):
        return Database.DATABASE[colllection].find(query)

    @staticmethod
    def find_one(colllection, query):
        return Database.DATABASE[colllection].find_one(query)