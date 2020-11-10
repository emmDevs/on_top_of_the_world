from db.run_sql import run_sql
import string

from models.city import City
from models.country import Country

import repositories.country_repository as country_repository

# SAVE CITY
def save(city):
    result = string.capwords(city.name)
    sql = "INSERT INTO cities(name, country_id, notes, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [result, city.country.id, city.notes, city.visited] 
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

# SELECT ALL CITIES
def select_all():
    cities = []
# I want to return the list of cities in alphabetical order
    sql = "SELECT * FROM cities ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['notes'], row['visited'], row['id'])
        cities.append(city)
    return cities

# SELECT CITY BY ID
def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['notes'], result['visited'], result['id'])
    return city

# SELECT CITY BY COUNTRY
def select_city_by_country(id):
    cities = []
    # I want to return the list of cities in alphabetical order
    sql = "SELECT * FROM cities WHERE country_id = %s ORDER BY name ASC"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['notes'], row['visited'], row['id'])
        cities.append(city)
    return cities

# UPDATE CITY
def update(city):
    result = string.capwords(city.name)
    sql = "UPDATE cities SET (name, country_id, notes, visited) = (%s, %s, %s, %s) WHERE id = %s"
    values = [result, city.country.id, city.notes, city.visited, city.id]
    print(values)
    run_sql(sql, values)


# SELECT ALL VISITED CITIES
def select_all_visited():
    cities = []
# I want to return the list of cities in alphabetical order
    sql = "SELECT * FROM cities WHERE visited = %s ORDER BY name ASC"
    values = [True]
    results = run_sql(sql, values)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['notes'], row['visited'], row['id'])
        cities.append(city)
    return cities

# SELECT ALL UNVISITED CITIES
def select_all_not_visited():
    cities = []
# I want to return the list of cities in alphabetical order
    sql = "SELECT * FROM cities WHERE visited is FALSE ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['notes'], row['visited'], row['id'])
        cities.append(city)
    return cities

# DELETE ALL CITIES
def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)    

# DELETE CITY BY ID
def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def yes_or_no(id):
#     sql = "SELECT visited FROM cities WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)
#     visited = result
#     if visited = True:
#         return yes
#     else:
#         return no