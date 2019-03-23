from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(100), unique=True)

    def __repr__(self):
    	return f"< User {username} >"
    	