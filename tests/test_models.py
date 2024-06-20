import unittest
from app.forms import RegistrationForm, LoginForm


class TestForms(unittest.TestCase):
    def test_registration_form(self):
        form = RegistrationForm(username='test_user', email='test@example.com', password='password', confirm_password='password')
        self.assertTrue(form.validate())

    # def test_login_form(self):
    #     form = LoginForm(
