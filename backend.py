from flask import Flask, request
import data
app = Flask(__name__)

@app.route("/")
def home():
    return 'Home'

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    data.getCredentials(username,password)

    return f'Logged in as {username}'

if __name__ == '__main__':
    app.run()
