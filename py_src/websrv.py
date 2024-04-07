from flask import Flask, render_template, request, redirect, session
import database
import sc_deployer
 
app = Flask(__name__)

bc = sc_deployer.sc_deployer()
dat = database.db()
# To render a login form 
@app.route('/')
def view_form():
    return render_template('page.html')
 

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    password = data['password'] 
    username = data['username']
    addr = dat.query_for_sc(username)
    if addr != 404:
        if bc.call_checker(addr):
            return "OK", 200
    else:
        return render_template('page.html')


@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        hash_str = data['hash_str']
        addr = bc.deploy(hash_str)
        dat.insert(username, addr)
        print(username, hash_str)
        return "OK", 200
 
if __name__ == '__main__':
    app.run()