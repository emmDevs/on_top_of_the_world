import unittest
from models.attraction import Attraction
from models.city import City
from models.country import Country

class TestAttraction(unittest.TestCase):

    def setUp(self):
        self.country = Country("France", "Europe")
        self.city = City("Paris", self.country)
        self.attraction = Attraction("Eiffel Tower", 25.90, self.city)

    def test_check_attraction_has_a_name(self):
        self.assertEqual("Eiffel Tower", self.attraction.name)

    def test_check_attraction_has_a_cost(self):
        self.assertEqual(25.90, self.attraction.cost)

    def test_check_attraction_has_a_city(self):
        self.assertEqual("Paris", self.attraction.city.name)

    def test_check_attraction_has_a_country(self):
        self.assertEqual("France", self.attraction.city.country.name)

    def test_check_attraction_has_a_continent(self):
        self.assertEqual("Europe", self.attraction.city.country.continent)