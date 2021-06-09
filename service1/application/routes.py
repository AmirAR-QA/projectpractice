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
    # if request.method == 'GET':
    #     return render_template("home.html", form=form)
    if form.validate_on_submit():
        get_encounter = requests.get('http://service2:5001/encounter')
        your_adventure = get_encounter.text
        get_location = requests.get('http://service3:5002/location')
        your_location = get_location.text
        result = requests.post('http://service4:5003/result', data=your_adventure)
        your_encounter = result.text
        data = Encounters(
                encounter = your_encounter,
                location = your_location,
                outcomes = result)
        db.session.add(data)
        db.session.commit()
        
        all_adventures = encounters.query.order_by(desc(encounters.id)).limit(5).all()

        return render_template('home.html', title='Class', form=form, encounter=your_adventure, location=your_location, result=result, all_adventures=all_adventures)