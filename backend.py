from flask import Flask, request
import data
app = Flask(__name__)

@app.route("/")
def home():
    test = data.getCredentials("test","test")
    return str(test)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    data.getCredentials(username,password)

    return f'Logged in as {username}'

if __name__ == '__main__':
    app.run()

@app.route('/intialize')
def intialize():
    data.intialize()

@app.route('/logcollection')
def logCollection():
    pass

@app.route('/update')
def update():
    pass
