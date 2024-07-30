import unittest
from app import app  # Adjust the import based on your project structure

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Adjust based on your homepage content

    def test_greeting_page(self):
        response = self.client.get('/greetings')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)  # Adjust based on your greeting page content

if __name__ == '__main__':
    unittest.main()

