from flask import Flask, render_template, request, url_for, Response
from application import app, db
from application.models import Encounters, Form
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import random, requests
from os import getenv

@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods = ['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        your_adventure = requests.get('http://service2:5001/encounter').text
        your_location = requests.get('http://service3:5002/location').text
        your_encounter = requests.post('http://service4:5003/result', data=your_adventure).text

        data2 = Encounters(encounter = your_adventure, location = your_location, outcomes = your_encounter)

        all_adventures = Encounters.query.order_by(desc(Encounters.id)).limit(5).all()

        db.session.add(data2)
        db.session.commit()

        return render_template('home.html', title='Class', form=form, encounter=your_adventure, location=your_location, result=your_encounter, all_adventures=all_adventures)

    return render_template('home.html', form=form)