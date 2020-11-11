from db.run_sql import run_sql
import string

from models.attraction import Attraction
from models.city import City
from models.country import Country

import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# Take user search input and return search results
def user_search_cities(search):
    user_search = string.capwords(search)
    search_results = []
    sql = "SELECT * FROM cities WHERE name = %s"
    values = [user_search]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['notes'], row['visited'], row['id'])
        search_results.append(city)
    return search_results

# def user_search(search):
#     user_search = string.capwords(search)
#     search_results = []
#     sql = "SELECT * FROM attractions WHERE name = %s UNION ALL SELECT * FROM cities where name %s UNION ALL SELECT * FROM countries WHERE name = %s"     
#     values = [user_search]
#     results = run_sql(sql, values)

#     for row in results:
#         result_attraction = attraction_repository.select(id)
#         attraction = Attraction(row['name'], row['cost'], city, row['id'])
#         result_city = city_repository.select(id)
#         city = City(row['name'], country, row['notes'], row['visited'], row['id'])
#         result_country = country_repository.select(id)
#         country = Country(row['name'], row['continent'], row['id'])
#         search_results.append(attraction)
#         search_results.append(city)
#         search_results.append(country)
#     return search_results
