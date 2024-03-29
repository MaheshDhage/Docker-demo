# app.py
from flask import Flask
from urllib.parse import quote

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Dockerized World!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
