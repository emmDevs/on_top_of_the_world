import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):

    def setUp(self):
        self.country = Country("France", "Europe")
        self.city = City("Paris", self.country, "cold in winter!")

    def test_check_city_has_a_name(self):
        self.assertEqual("Paris", self.city.name)

    def test_check_city_has_a_country(self):
        self.assertEqual("France", self.country.name)