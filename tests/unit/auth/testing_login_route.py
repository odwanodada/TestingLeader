from tests.base_test import BaseTest

class TestingLogin(BaseTest):
    def test_login_route(self):
        with self.app:
            response = self.app.get('/log-in', content_type = 'html/text')
            self.assertEqual(response.status_code, 200)
