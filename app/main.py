#!/usr/bin/env python

from flask import Flask

app = Flask(__name__)

# Main route
@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>'
