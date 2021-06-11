from flask_testing import TestCase
from flask import url_for
from service4.app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestQuery(TestBase):
    def test_service4(self):
        response = self.client.post(url_for('result'), data='a pack of firebreathing lizards')
        self.assert200(response)
        expected = ("you manage to escape the lizards, though a little singed","You engage in hours of intense diplomacy, the lizards have become your vassals! glory be to the lizard king!")
        self.assertEqual(response.data.decode('utf-8'), expected)