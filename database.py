import ssl

from pymongo import MongoClient


class Database:
    def __init__(self, connection_string):
        self.__connection_string = connection_string
        self.__database_name = None
        self.__client = None
        self.__db_handler = None
        self.__collection_handler = None

    def database_init(self, database_name):
        self.__database_name = database_name
        self.__client = MongoClient(self.__connection_string,ssl_cert_reqs=ssl.CERT_NONE)
        self.__db_handler = self.__client[self.__database_name]

    def set_collection(self, collection_name):
        self.__collection_handler = self.__db_handler[collection_name]
        return self.__collection_handler

    def insert(self,data):
        self.__collection_handler.insert_one(data)

    def exists(self,key,value):
        result = self.__collection_handler.find_one({key: value})
        if (result):
            return 1
        else:
            return 0
    def get(self,key,value,to_get):
        result = self.__collection_handler.find_one({key: value})
        return result[to_get]