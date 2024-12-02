from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "<h1> this is the main Page</h1>"