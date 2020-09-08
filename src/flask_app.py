from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "Welcome to your running flask instance!"