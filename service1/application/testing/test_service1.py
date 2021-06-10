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

class TestQuery(TestHome):
    def test_index(self):
        with mock() as mocks:
            form = Form
            test1 = self.client.get(url_for("home"))
            self.assert200(test1)
            mocks.get('http://service2:5001/encounter', text="a giant rat")
            mocks.get('http://service3:5002/location', text='in a cave')
            mocks.post('http://service4:5003/result', text='You manage to escape by sacrificing one of your boots')
            response = self.client.post(url_for("home"))
        self.assert200(response)
        self.assertIn("a giant rat", response.data.decode())