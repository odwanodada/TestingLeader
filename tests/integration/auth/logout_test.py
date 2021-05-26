
from tests.base_test import BaseTest
from flask import request
from flask_login import current_user, AnonymousUserMixin
from website.models import User
from tests.base_test import db


class TestLogOut(BaseTest):

    def test_logout_status_code(self):
        with self.app_context as c:
            c = self.app.get('/log-out', follow_redirects=True)

            self.assertEqual(c.status_code, 200)


    def test_logout_successful(self):
        with self.app:
            with self.app_context:


                response = self.app.post('/sign-up',
                                         data=dict(email="og@gmail.com", firstName="og", password1="1234567", password2="1234567"), follow_redirects=True)

                user = db.session.query(User).filter_by(email="og@gmail.com").first()

                self.assertTrue(user)

                self.assertIn(b'Account created', response.data)


                res = self.app.post('/log-in',
                                    data=dict(email="og@gmail.com", password="1234567"), follow_redirects=True)

                self.assertIn(b'Logged in successfully', res.data)

                self.assertEqual(res.status_code, 200)


                out = self.app.get('/log-out', follow_redirects=True)

                self.assertEqual(out.status_code, 200)



                self.assertEqual('http://localhost/log-in', request.url)



                self.assertEqual(current_user.get_id(), AnonymousUserMixin.get_id(self))

                print(AnonymousUserMixin.get_id(self))

                print(current_user.get_id())



                s = self.app.get('/log-out', follow_redirects=False)

                self.assertEqual(s.status_code, 302)

    def test_logout_not_successful(self):
        with self.app_context as c:

            c = self.app.get('/log-out', follow_redirects=False)

            self.assertEqual(c.status_code, 302)
