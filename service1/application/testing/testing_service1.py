from flask_testing import TestCase
from flask import url_for
import requests
from requests_mock import mock
from application import app, db
from application.models import Form

class TestHome(TestCase):
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"
        app.config['SECRET_KEY'] = "secret"
        app.config['WTF_CSRF_ENABLED'] = False
        db.drop_all()
        db.create_all()
        return app

class TestQuery(TestBase):
    def test_index(self):
        with mock() as mocks:
            form = Form
            b = self.client.get(url_for("home"))
            self.assert200(b)
            mocks.get('http://service_2:5001/encounter', text='a giant rat')
            mocks.get('http://service_3:5002/location', text='in a cave')
            mocks.post('http://service_4:5003/result', text='You manage to escape by sacrificing one of your boots')

            response = self.client.post(url_for("home"))

            
        self.assert200(response)
        self.assertIn("a giant rat", response.data.decode())