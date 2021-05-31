from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestLogIn(BaseTest):


    def test_sign_in(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/sign-up',
                                         data=dict(email="nodada@gmail.com", firstName="nodada",
                                                   password1="2244667", password2="2244667"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="nodada@gmail.com").first()


                self.assertTrue(user)

                self.assertIn(b'Account created', response.data)

                res = self.app.post('/log-in',
                                    data=dict(email="nodada@gmail.com", password="2244667"), follow_redirects=True)

                self.assertIn(b'Logged in successfully', res.data)

                self.assertEqual(res.status_code, 200)


    def test_email_unknown(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/sign-up',
                                         data=dict(email="nodada@gmail.com", firstName="nodada", password1="1011122", password2="1011122"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="nodada@gmail.com").first()

                self.assertTrue(user)

                res = self.app.post('/log-in',
                                    data=dict(email="nodda@gmail.com", password="1011122"), follow_redirects=True)

                self.assertIn(b'Email does not exist', res.data)

                self.assertEqual(res.status_code, 200)

                self.assertEqual('http://localhost/log-in', request.url)

    def test_invalid_password(self):
        with self.app:
            with self.app_context:
                response = self.app.post('/sign-up',
                                         data=dict(email="odwa@gmail.com", firstName="odwa", password1="1011122", password2="1011122"), follow_redirects=True)

                res = self.app.post('/log-in',
                                    data=dict(email="odwa@gmail.com", password="10111"))

                self.assertIn(b'alert', res.data)
                self.assertNotEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

         
