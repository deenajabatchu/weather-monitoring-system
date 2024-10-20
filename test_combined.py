# tests/test_combined.py

import unittest
from unittest.mock import patch, MagicMock
import requests

# Assume we have the following functions in our main application
from main import get_weather_data, process_weather_data, check_alerts


class TestWeatherMonitoringSystem(unittest.TestCase):

    # Test cases for API integration
    @patch('requests.get')
    def test_get_weather_data(self, mock_get):
        # Mocking the API response
        mock_response = MagicMock()
        mock_response.json.return_value = {
            'main': {
                'temp': 280.32,
                'feels_like': 279.15,
            },
            'weather': [{'main': 'Clear'}],
            'dt': 1618317040
        }
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        # Call the function
        data = get_weather_data('CityName', 'API_KEY')
        
        # Check if data is parsed correctly
        self.assertEqual(data['temp'], 280.32)
        self.assertEqual(data['feels_like'], 279.15)
        self.assertEqual(data['weather'][0]['main'], 'Clear')
        self.assertEqual(data['dt'], 1618317040)

    # Test cases for data processing functions
    def test_process_weather_data(self):
        sample_data = {
            'temp': 280.32,
            'feels_like': 279.15,
            'weather': [{'main': 'Clear'}],
            'dt': 1618317040
        }
        processed_data = process_weather_data(sample_data)
        
        # Verify temperature conversion (from Kelvin to Celsius)
        self.assertAlmostEqual(processed_data['temp'], 7.17, places=2)  # 280.32K to Celsius
        self.assertAlmostEqual(processed_data['feels_like'], 6.00, places=2)  # 279.15K to Celsius

    # Test cases for alerting logic
    def test_check_alerts(self):
        current_temp = 36  # example temperature in Celsius
        threshold = 35
        alert = check_alerts(current_temp, threshold)
        
        # Check if the alert is triggered correctly
        self.assertTrue(alert)

        # Test with a temperature below the threshold
        current_temp = 34
        alert = check_alerts(current_temp, threshold)
        
        # Check that no alert is triggered
        self.assertFalse(alert)


if __name__ == '__main__':
    unittest.main()