"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy as sqla


# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = sqla()


##############################################################################
# Model definitions

class User(db.Model):
    """User of PuppyCrazed"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_fname = db.Column(db.String(63), nullable=True)
    user_lname = db.Column(db.String(64), nullable=True)
    user_email = db.Column(db.String(64), nullable=True, unique=True)
    user_password = db.Column(db.String(64), nullable=True)
    pet_img = db.Column(db.String(255), nullable=True)
    pet_name = db.Column(db.String(64), nullable=True)
    pet_name = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        """Displays useful info about the Parent object."""
        return ("<User user_id:{} user_fname:{}, user_lname:{}," +
                " pet_img:{}").format(self.user_id,
                                      self.user_fname,
                                      self.user_lname,
                                      self.pet_img)


class View(db.Model):
    """Table storing who has viewed whom and whether they liked them or not."""

    __tablename__ = "views"

    view_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    viewer_id = db.Column(db.Integer,
                          db.ForeignKey("users.user_id"),
                          nullable=False)
    viewed_id = db.Column(db.Integer,
                          db.ForeignKey("users.user_id"),
                          nullable=False)

    viewer = db.relationship("User", foreign_keys=[viewer_id])

    viewed = db.relationship("User", foreign_keys=[viewed_id])

    def __repr__(self):
        """Displays view info"""
        return "<View view_id:{}>".format(self.view_id)




##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///puppycrazed'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from PuppyCrazed import app
    connect_to_db(app)
    db.create_all()
    print "Connected to DB."
