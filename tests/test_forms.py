import unittest
from app import app, db
from app.models import User


class TestUserModel(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_user_creation(self):
        user = User(username='test_user', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)


if __name__ == '__main__':
    unittest.main()
