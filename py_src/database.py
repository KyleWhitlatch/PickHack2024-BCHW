from pymongo import MongoClient
import json

class testmongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['login_db']
        self.users = self.db['users']
        self.posts = self.db.posts
        
    def store_userpass(self, username, address):
        post = {"username": username, "sc_address": address}
        id = self.users.insert_one(post).inserted_id
        print(id)
        
    def retrieve_userpass(self, username):
        user = self.users.find_one({'username': username})
        return user
        
        
test = testmongo()
test.store_userpass('test_user', 'test_address')
query = test.retrieve_userpass('test_user')
print(query['sc_address'])
