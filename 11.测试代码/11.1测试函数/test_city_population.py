import unittest
from city_country_population import city_country
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        city_coun = city_country("Paris", "France")
        self.assertEqual(city_coun, "Paris, France - population 5000000")

    def test_city_country_population(self):
        city_coun_popu = city_country("Paris", "France", "1000000")
        self.assertEqual(city_coun_popu, "Paris, France - population 1000000")

unittest.main()