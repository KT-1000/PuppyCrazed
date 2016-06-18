from flask import Flask, render_template, redirect
from model import View, User

import random

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/matches')
def match():

    view_id = random.choice(user_ids
        )
    return render_template("match.html", view_id=view_id)


@app.route('/like.json')
def like():

    viewed_id = request.form.get(viewed_id)
    like = request.form.get(like)
    viewer_id = session.get(user_id)

    view = View(viewer_id=viewer_id,
                viewed_id=viewed_id,
                like=like)

    db.session.add(view)
    db.sesssion.commit()

    user_ids = User.query.all()
    for user_id in user_ids:
        if user_id == viewed_id:
            user_ids.remove(user_id)
        elif user_id == viewer_id:
            user_ids.remove(user_id)

    view_id = random.choice(user_ids)

    return jsonify({"view_id": view_id)


if __name__ == '__main__':
    app.run()
