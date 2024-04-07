import sqlite3
import json

class db:
    def __init__(self):
        self.con = sqlite3.connect('users.db', check_same_thread=False)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE users(username, sc_address)")
    
    def insert(self, user, addr):
        self.cur.execute(f'INSERT INTO users VALUES (\'{str(user)}\',\'{str(addr)}\')')
        self.con.commit()
    
    def query_for_sc(self, user):
        res = self.cur.execute(f'SELECT sc_address FROM users WHERE username=\'{str(user)}\'')
        return res.fetchone()
        
            
        
# Test the database functions
# test = testmongo()
# test.store_userpass('test_user', 'test_address')
# query = test.retrieve_userpass('test_user')
# print(query['sc_address'])
