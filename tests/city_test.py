import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):

    def setUp(self):
        self.country = Country("France", "Europe")
        self.country2 = Country("Italy", "Europe")
        self.city = City("Paris", self.country, "cold in winter!")
        self.city2 = City("Rome", self.country2)

    def test_check_city_has_a_name(self):
        self.assertEqual("Paris", self.city.name)

    def test_check_city_has_a_country(self):
        self.assertEqual("France", self.country.name)

    def test_check_city_has_notes(self):
        self.assertEqual("cold in winter!", self.city.notes)

    def test_check_city_has_notes__no_notes(self):
        self.assertEqual(None, self.city2.notes)

    def test_check_city_has_been_visited__false(self):
        self.assertEqual(False, self.city.visited)