from flask_testing import TestCase
from flask import url_for
from application import app

class TestHome(TestCase):
    def create_app(self):
        return app

class TestQuery(TestHome):
    def test_service3(self):
        
        response = self.client.get(url_for("location"))

        alllocations = ["in a forested valley","on top of a mountain","in a cave","on the outskirts of a city","while walking into a swamp"]
        self.assertIn(response.data.decode(), alllocations)