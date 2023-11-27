Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
... from app import app
... 
... class FlaskTestCase(unittest.TestCase):
... 
...     def setUp(self):
...         app.testing = True
...         self.app = app.test_client()
... 
...     def test_index(self):
...         response = self.app.get('/')
...         self.assertEqual(response.status_code, 200)
...         self.assertIn(b'Welcome to the Flask App', response.data)
... 
... if __name__ == '__main__':
...     unittest.main()
