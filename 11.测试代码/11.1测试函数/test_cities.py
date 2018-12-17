import unittest
from city_functions import city_country
#继承unittest下的TestCase
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        citCountry = city_country("Beijing", "China")
        self.assertEqual(citCountry, "Beijing, China")

unittest.main()
