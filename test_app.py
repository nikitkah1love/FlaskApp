import unittest
from app import app, db
from models import User
from werkzeug.security import check_password_hash

class FlaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up the application and test client
        cls.app = app
        cls.client = cls.app.test_client()
        cls.app.config['TESTING'] = True
        cls.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        # Create the database and tables
        with cls.app.app_context():
            db.create_all()

    @classmethod
    def tearDownClass(cls):
        # Drop the database after tests are done
        with cls.app.app_context():
            db.drop_all()

    def test_register_page(self):
        response = self.client.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)  # Check that the registration page is loaded

    def test_login_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)  # Check that the login page is loaded

    def test_register_user(self):
        response = self.client.post('/register', data={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # Assuming no redirect
       # self.assertIn(b'<li class="success">Registration successful! You can now log in.</li>', response.data)

        # Verify the user was added to the database
        user = User.query.filter_by(username='testuser').first()
        self.assertIsNotNone(user)
        self.assertTrue(check_password_hash(user.password, 'testpassword'))

    def test_login_user(self):
        # Register a user first
        self.client.post('/register', data={
            'username': 'testloginuser',
            'password': 'testloginpassword'
        })

        # Test login
        response = self.client.post('/login', data={
            'username': 'testloginuser',
            'password': 'testloginpassword'
        })
        self.assertEqual(response.status_code, 302)  # Assuming no redirect
      #  self.assertIn(b'Login successful!', response.data)

    def test_invalid_login(self):
        # Attempt to log in with invalid credentials
        response = self.client.post('/login', data={
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Invalid credentials. Please try again.', response.data)

if __name__ == '__main__':
    unittest.main()

