import unittest
from datetime import datetime
from src.processing.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = DataProcessor()

    def test_process_weather_data(self):
        test_data = {
            'weather': [{'main': 'Clear'}],
            'main': {'temp': 25, 'feels_like': 26},
            'dt': int(datetime.now().timestamp())
        }
        self.processor.process_weather_data('TestCity', test_data)
        # Add assertions to check if data was processed correctly

    def test_get_daily_summary(self):
        summary = self.processor.get_daily_summary('TestCity', '2024-01-01')
        self.assertIsNotNone(summary)
        # Add more assertions to check summary contents

if __name__ == '__main__':
    unittest.main()