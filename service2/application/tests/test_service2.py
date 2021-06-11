from flask_testing import TestCase
from flask import url_for
from application import app

class TestHome(TestCase):
    def create_app(self):
        return app

class TestQuery(TestHome):
    def test_service2(self):
        
        response = self.client.get(url_for("encounter"))

        allencounters = ["a giant rat","a giant goat","a pack of firebreathing lizards","a very small dwarf","an evil pig summoning wizard"]
        self.assertIn(response.data.decode(), allencounters)