import unittest
from src.storage.database import Database
from datetime import datetime

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    def test_insert_and_retrieve_data(self):
        test_data = {
            'city': 'TestCity',
            'main': 'Clear',
            'temp': 25.5,
            'feels_like': 26.0,
            'dt': datetime.now()
        }
        self.db.insert_weather_data(test_data)

        retrieved_data = self.db.get_daily_data('TestCity', test_data['dt'].date().isoformat())
        self.assertIsNotNone(retrieved_data)
        self.assertEqual(len(retrieved_data), 1)
        # Add more assertions to check retrieved data

    def tearDown(self):
        self.db.close()

if __name__ == '__main__':
    unittest.main()