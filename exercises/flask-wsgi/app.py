from flask import Flask


app = Flask(__name__)


@app.route('/')  # '/' means home page of application http://www.example.com/
def home():
    return 'Hello world!'


app.run(port=8080)
