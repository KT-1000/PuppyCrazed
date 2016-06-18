from flask import Flask, render_template, redirect, session
from model import View, User, connect_to_db


import random

app = Flask(__name__)

app.secret_key = "ABC"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def home():

    session["user_id"] = 1
    user = User.query.get(1)
    matches = user.matches()
    return render_template("home.html", matches=matches)


@app.route('/matches')
def match():

    session["user_id"] = 1

    users = User.query.all()
    user_ids = []
    for user in users:
        user_ids.append(user.user_id)
    for user_id in user_ids:
        if user_id == viewer_id:
            user_ids.remove(user_id)

    view_id = random.choice(user_ids)

    view = User.query.filter_by(user_id=view_id).one()

    return render_template("match.html", view=view)


@app.route('/like.json')
def like():

    viewed_id = request.form.get(viewed_id)
    like = request.form.get(like)

    viewer_id = session.get("user_id")

    view = View(viewer_id=viewer_id,
                viewed_id=viewed_id,
                like=like)

    db.session.add(view)
    db.sesssion.commit()

    users = User.query.all()
    user_ids = []
    for user in users:
        user_ids.append(user.user_id)
    for user_id in user_ids:
        if user_id == viewed_id:
            user_ids.remove(user_id)
        elif user_id == viewer_id:
            user_ids.remove(user_id)

    view_id = random.choice(user_ids)

    view = User.query.filter_by(user_id=view_id).one()

    return jsonify({"view_id": view})


if __name__ == '__main__':
    connect_to_db(app)
    app.run()
