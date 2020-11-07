import pdb
from models.country import Country
from models.city import City
from models.attraction import Attraction
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository
import repositories.attraction_repository as attraction_repository

country_repository.delete_all()
city_repository.delete_all()
attraction_repository.delete_all()



pdb.set_trace()