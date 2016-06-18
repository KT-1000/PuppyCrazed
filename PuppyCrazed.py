from flask import Flask, render_template, redirect
from model import View, User

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/matches')
def match():
    return render_template("match.html")


@app.route('/like')
def like():
    return redirect()


if __name__ == '__main__':
    app.run()
