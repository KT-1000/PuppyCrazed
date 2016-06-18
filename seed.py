"""Utility file to seed the birthdate_game database with fake data"""

from model import User, View

from model import connect_to_db, db
from PuppyCrazed import app


def load_users():
    """Load sample data elements"""

    jimmy = User(user_fname="Jimmy",
                 user_lname="Peterson",
                 user_email="nickl@gmail.com",
                 user_password="password")

    martha = User(user_fname="Martha",
                  user_lname="King",
                  user_email="martha@gmail.com",
                  user_password="password")

    joseph = User(user_fname="Joseph",
                  user_lname="Marshall",
                  user_email="joseph@gmail.com",
                  user_password="password")
    # Add objects to session
    db.session.add_all([jimmy, martha, joseph])
    # Commit changes to database
    db.session.commit()


def load_views():
    """Load sample views"""
    jimmy_like_martha = View(viewer_id=1,
                             viewed_id=2,
                             like=True)
    martha_like_jimmy = View(viewer_id=2,
                             viewed_id=1,
                             like=True)
    joseph_like_martha = View(viewer_id=3,
                              viewed_id=2,
                              like=False)

    db.session.add_all([jimmy_like_martha, martha_like_jimmy, joseph_like_martha])
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_views()
