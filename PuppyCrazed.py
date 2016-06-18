from flask import Flask
from model import connect_to_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':

    connect_to_db(app)
    app.run()
