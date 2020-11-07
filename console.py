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

france = Country("France", "Europe")
country_repository.save(france)
italy = Country("Italy", "Europe")
country_repository.save(italy)
america = Country("America", "North America")
country_repository.save(america)
peru = Country("Peru", "South America")
country_repository.save(peru)

paris = City("Paris", france)
city_repository.save(paris)
rome = City("Rome", italy)
city_repository.save(rome)
venice = City("Venice", italy)
city_repository.save(venice)
new_york_city = City("New York City", america)
city_repository.save(new_york_city)
lima = City("Lima", peru)
city_repository.save(lima)

eiffel_tower = Attraction("Eiffel Tower", 25.90, paris)
attraction_repository.save(eiffel_tower)
the_louvre = Attraction("The Louvre", 17, paris)
attraction_repository.save(the_louvre)
the_colosseum = Attraction("The colosseum", 12, rome)
attraction_repository.save(the_colosseum)
st_marks_basilica = Attraction("Saint Mark's Basilica", 3, venice)
attraction_repository.save(st_marks_basilica)
central_park = Attraction("Central Park", 0, new_york_city)
attraction_repository.save(central_park)
natural_history_mueseum = Attraction("Natural History Museum", 23, new_york_city)
attraction_repository.save(natural_history_mueseum)
huaca_pucllana = Attraction("Huaca Pucllana", 15, peru)
attraction_repository.save(huaca_pucllana)

pdb.set_trace()