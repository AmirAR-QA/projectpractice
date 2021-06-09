from application import app
from flask import Flask, Response
import random

@app.route('/encounter', methods=['GET'])
def encounter():
    encounter = ("a giant rat","a giant goat","a pack of firebreathing lizards","a very small dwarf","an evil pig summoning wizard")
    random_encounters = random.choice(encounter)
    return Response(random_encounters)