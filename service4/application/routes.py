from flask import redirect, url_for, request, Response, jsonify
from application import app
import random, requests

@app.route('/result', methods = ['GET', 'POST'])
def returnresult():
    encounter_result = "This encounter has been censored because of excessive silliness"
    encounters = request.data.decode('utf-8')

    outcomes_rat = ["You manage to escape by sacrificing one of your boots","you've tamed the rat, glory be to the great rat rider!"]
    outcomes_goat = ["You somehow you manage to annoy the incredibly wise ancient goat, you've been cursed with a goats beard on your elbows!","he just ignores you, what an old goat!"]
    outcomes_lizards = ["You engage in hours of intense diplomacy, the lizards have become your vassals! glory be to the lizard king!","you manage to escape the lizards, though a little singed"]
    outcomes_dwarf = ["You let the dwarf eat all your supplies, roll a survival check","the dwarf has gifted you an axe of braiding!"]
    outcomes_wizard = ["You have been transformed into one of the wizards pigs","you defeat the wizard, and loot his staff of pig summoning!"]

    if encounters == "a giant rat":
        encounter_result = random.choice(outcomes_rat)
    elif encounters == "a wise old goat":
        encounter_result = random.choice(outcomes_goat)
    elif encounters == "a pack of firebreathing lizards":
        encounter_result = random.choice(outcomes_lizards)
    elif encounters == "a particularly portly dwarf":
        encounter_result = random.choice(outcomes_dwarf)
    elif encounters == "an evil pig summoning wizard":
        encounter_result = random.choice(outcomes_wizard)   

    return Response(encounter_result)