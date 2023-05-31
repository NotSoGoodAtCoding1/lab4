import unittest
from flask import Flask, request
from main import form


class TestForm(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_form_with_zero_discriminant(self):
        with self.client as c:
            response = c.post('/', data={'num_1': '1', 'num_2': '4', 'num_3': '4'})
            self.assertEqual(response.status_code, 200)
            self.assertIn(response.data, '0.0')

    def test_form_with_negative_discriminant(self):
        with self.client as c:
            response = c.post('/', data={'num_1': '1', 'num_2': '2', 'num_3': '3'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, 'Дискрименант меньше нуля')

    def test_form_with_positive_discriminant(self):
        with self.client as c:
            response = c.post('/', data={'num_1': '1', 'num_2': '2', 'num_3': '1'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, '0.0\n-1.0')


if __name__ == '__main__':
    unittest.main()