from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestSignUp(BaseTest):
    def test_sign_up(self):
        with self.app_context as c:
            c = self.app.get('/sign-up', follow_redirects=True)

            self.assertEqual(c.status_code, 200)

    def test_sign_up_Two(self):
        with self.app:
            response = self.app.get('/sign-up', follow_redirects=True)

            self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

            self.assertIn('/sign-up', request.url)

            self.assertIn(b'<title>\nSign Up\n</title>', response.data)

            self.assertEqual(response.status_code, 200)

    def test_post_email_handle(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="odw", first_name="Odwa",password1="10111", password2="10111"), follow_redirects=True)

            self.assertIn(b'Email must be greater than 3 characters', response.data)

            self.assertEqual(response.status_code, 200)

            user = db.session.query(User).filter_by(email="meh").first()

            self.assertFalse(user)

            self.assertIsNone(current_user.get_id())



    def test_sign_up_short_name(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="od", firstName="Odwa", password1="10111", password2="10111"), follow_redirects=True)
            self.assertIn(b'First name must be greater than 1 character', response.data)

    def test_password_dont_match(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="odwa@gmail.com", firstName="Odwa", password1="1234abc", password2="1234"), follow_redirects=True)
            self.assertIn(b'Passwords don&#39;t match', response.data)

    def test_sign_up_success(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="odwa@gmail.com", firstName="Odwa", password1="10111abc", password2="10111abc"), follow_redirects=True)

            user = db.session.query(User).filter_by(email="odwa@gmail.com").first()

            self.assertTrue(user)

            self.assertIn(b'Account created', response.data)

    # Added this test
    def test_password_seven_chara(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="odwa@gmail.com", firstName="Odwa", password1="10111ab", password2="10111ab"), follow_redirects=True)
            self.assertIn(b'Password must be at least 7 characters', response.data)
            self.assertEqual(response.status_code, 200)

    # Added this test too
    def test_user_already_exists(self):
        with self.app:
            response = self.app.post('/sign-up',
                                    data=dict(email="odwa@gmail.com", firstName="Odwa", password1="10111", password2="10111"), follow_redirects=True)

            user = db.session.query(User).filter_by(email="odwa@gmail.com")

            self.assertTrue(user)


    def test_seven_char(self):
        with self.app:
            response = self.app.post('/sign-up',
                                     data=dict(email="nodadaa@gmail.com", firstName="Nodadaa", password1="10111", password2="10111"), follow_redirects=True)
            self.assertIn(b'Password must be at least 7 characters', response.data)
            self.assertEqual(response.status_code, 200)


    def test_already_exists(self):
        with self.app:
            response = self.app.post('/sign-up',
                                    data=dict(email="odwa@gmail.com", firstName="Odwa", password1="abc10111", password2="abc10111"), follow_redirects=True)

            user = db.session.query(User).filter_by(email="odwa@gmail.com")

            self.assertTrue(user)

            response = self.app.post('/sign-up',
                                     data=dict(email="odwa@gmail.com", firstName="Odwa", password1="abc10111", password2="abc10111"), follow_redirects=True)

            self.assertIn(b'Email already in use', response.data)


