from flask_testing import TestCase
from flask import url_for
from application import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestQuery(TestBase):
    def test_service4(self):
        response = self.client.post(url_for('home'), data='a pack of firebreathing lizards,on the outskirts of a city')
        self.assert200(response)
        expected = "Oh no, you've run in to a pack of firebreathing lizards in on the outskirts of a city! What's going to happen? Aaaaaah! you manage to escape the lizards, though a little singed"
        self.assertEqual(response.data.decode('utf-8'), expected)