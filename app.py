import os
import random

from flask import Flask
from flask import render_template
import socket

app = Flask(__name__)

@app.route("/")
def main():
    print(color)
    return render_template('index.html', name=socket.gethostname(), color=color_codes[color])

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
