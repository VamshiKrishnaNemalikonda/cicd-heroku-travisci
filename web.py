from flask import Flask
app = Flask(__name__)

@app.route('/')

def index():
  return 'hello, world - Heroku + Github integration - CICD!'
