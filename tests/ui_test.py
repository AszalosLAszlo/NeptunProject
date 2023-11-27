Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from selenium import webdriver
... import unittest
... 
... class TestAppUI(unittest.TestCase):
... 
...     def setUp(self):
...         self.browser = webdriver.Chrome()
... 
...     def test_title(self):
...         self.browser.get('http://localhost:5000')
...         self.assertEqual(self.browser.title, 'Welcome')
... 
...     def tearDown(self):
...         self.browser.quit()
... 
... if __name__ == '__main__':
...     unittest.main()
