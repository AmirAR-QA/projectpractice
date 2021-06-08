from application import db

class Encounters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encounter = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    outcome = db.Column(db.String(500), nullable=False)