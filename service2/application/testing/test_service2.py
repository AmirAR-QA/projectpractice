from flask_testing import TestCase
from flask import url_for
import requests
from requests_mock import mock
from application import app

class TestBase(TestCase):
    def create_app(self):
        app.config.update(DEBUG = True)
        return app

class TestQuery(TestCase):
    def test_service2(self):
        
        response = self.client.get(url_for("encounter"))

        allencounters = ["a giant rat","a giant goat","a pack of firebreathing lizards","a very small dwarf","an evil pig summoning wizard"]
        self.assertIn(response.data.decode(), allencounters)