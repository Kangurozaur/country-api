import unittest
import json
from app import app

class TestCountryAPI(unittest.TestCase):
    def test_valid_country(self):
        with app.test_client() as client:
            response = client.get('/country/United States')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['continent'], 'North America')
            
    def test_invalid_country(self):
        with app.test_client() as client:
            response = client.get('/country/Invalid Country')
            data = json.loads(response.get_data(as_text=True))
            self.assertEqual(response.status_code, 404)
            self.assertEqual(data['error'], 'Invalid country name')

if __name__ == '__main__':
    unittest.main()
