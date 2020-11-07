from db.run_sql import run_sql

from models.city import City
from models.country import Country

def save(city):
    sql = "INSERT INTO cities(name, country, notes, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [city.name, city.country.id, city.notes, city.visited] 
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []
# I want to return the list of cities in alphabetical order
    sql = "SELECT * FROM cities ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        city = City(row['name'], row['country'], row['notes'], row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = City(result['name'], result['country'], result['notes'], result['visited'], result['id'])
    return city

def select_city_by_country(country):
    cities = []
    # I want to return the list of cities in alphabetical order
    sql = "SELECT * FROM cities WHERE country_id = %s ORDER BY name ASC"
    values = [country.id]
    results = run_sql(sql, values)

    for row in results:
        city = City(row['name'], row['country'], row['notes'], row['visited'], row['id'])
        cities.append(city)
    return cities

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)    