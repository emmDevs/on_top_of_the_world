import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("France", "Europe")

    def test_country_has_a_name(self):
        self.assertEqual("France", self.country.name)

    def test_country_has_a_continent(self):
        self.assertEqual("Europe", self.country.continent)