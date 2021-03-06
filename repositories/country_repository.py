from db.run_sql import run_sql
import string

from models.country import Country

# SAVE COUNTRY
def save(country):
    result = string.capwords(country.name)
    sql = "INSERT INTO countries(name, continent) VALUES ( %s, %s ) RETURNING id"
    values = (result, country.continent)
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

# SELECT ALL COUNTRIES
def select_all():
    countries = []
# when I list countries I want them to be alphabetical order each time
    sql = "SELECT * FROM countries ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['continent'], row['id'])
        countries.append(country)
    return countries

# SELECT COUNTRY BY ID
def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['continent'], result['id'])
    return country

# UPDATE COUNTRY
def update(country):
    result = string.capwords(country.name)
    sql = "UPDATE countries SET (name, continent) = (%s, %s) WHERE id = %s"
    values = [result, country.continent, country.id]
    print(values)
    run_sql(sql, values)

# DELETE ALL COUNTRIES
def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

# DELETE COUNTRY BY ID
def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# def select_country_from_city(id):
#     def select_city_by_country(id):
#     cities = []
#     # I want to return the list of cities in alphabetical order
#     sql = "SELECT * FROM cities WHERE country_id = %s ORDER BY name ASC"
#     values = [id]
#     results = run_sql(sql, values)

#     for row in results:
#         city = City(row['name'], row['country_id'], row['notes'], row['visited'], row['id'])
#         cities.append(city)
#     return cities