# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = 'aacuser' 
        PASS = 'CS340' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            try:
                result = self.collection.insert_one(data)  
                if result.inserted_id:
                    return True
                return False
            except Exception as e:
                print(f"Creat Error: {e}")
                return False
        else:
            raise Exception("Nothing to save")
            
    # Complete this read method to implement the R in CRUD.
    def read(self, searchData=None):
        try:
            # If search information is provided then filter otherwise return all
            if searchData:
                cursor = self.collection.find(searchData, {"_id": False})
            else:
                cursor = self.collection.find({}, {"_id": False})
                
            return list(cursor)
            
        except Exception as e:
            print(f"Read Error: {e}")
            # Return an empty list if fail 
            return []
        

    # Complete this update method to implement the U in CRUD.
    def update(self, searchData, updateData, many=False):
        if searchData is not None and updateData is not None:
            try:
                if many:
                    result = self.collection.update_many(searchData, updateData)
                else:
                    result = self.collection.update_one(searchData, updateData)

                return result.modified_count

            except Exception as e:
                print(f"Update Error: {e}")
                return 0
        else:
            raise Exception("Nothing to update")

    # Complete this delete method to implement the D in CRUD.
    def delete(self, searchData, many=True):
        if searchData is not None:
            try:
                if many:
                    result = self.collection.delete_many(searchData)
                else:
                    result = self.collection.delete_one(searchData)

                return result.deleted_count

            except Exception as e:
                print(f"Delete Error: {e}")
                return 0
        else:
            raise Exception("Nothing to delete")