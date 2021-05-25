from unittest import TestCase
from flask_login import current_user
from website.models import User
from tests.base_test import BaseTest, db

class TestLogin(BaseTest):
    def test_login(self):
         with self.app:
            response = self.app.post('/sign-login',
                                    data=dict(email='email@gmail.com',passwordEntered ='pass1234'),
                                    follow_redirects=True)
            # assert that new user is created in db
            user = db.session.query(User).filter_by(email='email@gmail.com').first()
            self.assertTrue(user)

         
