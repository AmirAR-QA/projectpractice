from application import db
from flask_wtf import FlaskForm
from wtforms import SubmitField

class Encounters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    encounter = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    outcomes = db.Column(db.String(500), nullable=False)

class Form(FlaskForm):
    adventuring = SubmitField("What lies ahead?")