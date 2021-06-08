from application import app
from flask import Flask, Response
import random

@app.route('/location', methods=['GET'])
def location():
    locations = ("in a forested valley","on top of a mountain","in a cave","on the outskirts of a city","while walking into a swamp")
    random_locations = random.choice(locations)
    return Response(random_locations)