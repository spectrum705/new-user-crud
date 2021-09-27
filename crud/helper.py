from pymongo import MongoClient


# cluster =  os.environ["mongoDb"]

class Database:
    def __init__(self, uri):

        self.uri = uri
        client = MongoClient(self.uri)
        db = client.crud
        self.collection= db.users

    def add(self, user):
        self.collection.insert_one(user)
        print("file uploaded:" )

    def retrieve(self, query, value):
        # query=query.split('=')
        reportData = self.collection.find({query:value})
        users=[]
        for i in reportData:
            del i["_id"]
            del i["pwd"]
            users.append(i)

        return users#[i for i,  del i['_id'] in reportData]
  
    def update(self, query, old_value, new_value, new_query= ""):

        self.collection.update_one({query:old_value},  { "$set": { new_query if new_query else query : new_value} })
        print("updated")


    def delete(self, query, value):
        reportData = self.collection.remove({query:value})
        print("data removed")




