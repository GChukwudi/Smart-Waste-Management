import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)

    def test_profile(self):
        response = self.app.get('/profile')
        self.assertEqual(response.status_code, 302)

    def test_admin(self):
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 302)

    def test_user(self):
        response = self.app.get('/user')
        self.assertEqual(response.status_code, 302)

        
if __name__ == '__main__':
    unittest.main()