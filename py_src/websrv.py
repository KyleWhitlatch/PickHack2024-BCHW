from flask import Flask, render_template, request, redirect, session
import database
 
app = Flask(__name__)
#app = Flask(static_folder='C:\\Users\\ltkli\\Documents\\GitHub\\PickHack2024-BCHW\\py_src\\static')
 
# Set a secret key for encrypting session data
app.secret_key = 'my_secret_key'
 
# dictionary to store user and password
users = {
    'kunal': '1234',
    'user2': 'password2'
}
dat = database.testmongo()
# To render a login form 
@app.route('/')
def view_form():
    return render_template('page.html')
 
# For handling get request form we can get
# the form inputs value by using args attribute.
# this values after submitting you will see in the urls.
# e.g http://127.0.0.1:5000/handle_get?username=kunal&password=1234
# this exploits our credentials so that's 
# why developers prefer POST request.
    

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password'] 
    username = data['username']
    user_name = dat.retrieve_username(username)
    if user_name != None  and dat.retrieve_userpass(username) != None:
        for i in user_name:
            #if i[password] == password:
            #return '', 200
            continue
    else:
        return render_template('page.html')


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        hash_str = data['hash_str']
        print(username, hash_str)
 
if __name__ == '__main__':
    app.run()