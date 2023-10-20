from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def hello_message():
    return {"message":"hello"}
