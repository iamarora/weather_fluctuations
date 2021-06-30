import unittest

from src.weather import Weather


class TestWeatherMethods(unittest.TestCase):
    def setUp(self):
        # Load the data for tests.
        self.weather_obj = Weather()
        self.weather_obj.load_data('data/data.csv')

    def test_data_loaded(self):
        self.assertIsNotNone(self.weather_obj.data)
        self.assertIsNotNone(self.weather_obj.lowest_temperature_row)
        self.assertIsNotNone(self.weather_obj.highest_fluctuation_station)

    def test_minimum_temperature_station_date(self):
        data = self.weather_obj.get_minimum_temperature_station_date()
        self.assertEqual(data['station_id'], '676223')
        self.assertEqual(data['date'], 2010.542)

    def test_maximum_fluctuation_station(self):
        self.assertEqual(self.weather_obj.get_maximum_fluctuation_station(), '735181')

    def test_maximum_fluctiation_date_range(self):
        self.assertEqual(self.weather_obj.get_maximum_fluctiation_date_range(2017.625, 2018.708), '459413')
