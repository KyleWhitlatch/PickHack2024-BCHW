from pymongo import MongoClient

# Create a client to connect to MongoDB
client = MongoClient('localhost', 27017)

# Create a new database
db = client['login_db']

# Create a collection named 'users'
users = db['users']

# Function to store a new username
def store_username(username):
    # Check if the username already exists
    if users.find_one({'username': username}):
        return "Username already exists"
    else:
        # Insert the new username
        users.insert_one({'username': username})
        return "Username stored successfully"

def store_hashed_password(password):
    # Check if the password already exists
    if users.find_one({'password': password}):
        return "Password already exists"
    else:
        # Insert the new password
        users.insert_one({'password': password})
        return "Password stored successfully"

def store_hash(hash):
    # Check if the hash already exists
    if users.find_one({'hash': hash}):
        return "Hash already exists"
    else:
        # Insert the new hash
        users.insert_one({'hash': hash})
        return "Hash stored successfully"
    
# print(store_username('test_user'))