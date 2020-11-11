from db.run_sql import run_sql

from models.attraction import Attraction
from models.city import City
from models.country import Country

import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

# Take user search input and return search results
def user_search_cities(search):
    search_results = []
    sql = "SELECT * FROM cities WHERE name = %s"
    values = [search]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['notes'], row['visited'], row['id'])
        search_results.append(city)
    return search_results

# def user_search(search):
#     search_results = []
#     sql = "SELECT * FROM attractions WHERE attraction.name LIKE % %s % UNION ALL SELECT * FROM cities where city.name LIKE % %s % UNION ALL SELECT * FROM countries WHERE countries.name like % %s %"     values = [search]
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
#     return render_template('search.html', search_results = search_results)

