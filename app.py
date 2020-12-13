from flask import Flask, render_template

import pymongo
 
client = pymongo.MongoClient("mongodb+srv://testuser:testuser@cluster0.uqb77.mongodb.net/auth?retryWrites=true&w=majority")
db = client.test
 
app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("register.html")

if __name__ == '__main__':
    app.run()
