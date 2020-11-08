from db.run_sql import run_sql

from models.country import Country

def save(country):
    sql = "INSERT INTO countries(name, continent) VALUES ( %s, %s ) RETURNING id"
    values = (country.name, country.continent)
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []
# when I list countries I want them to be alphabetical order each time
    sql = "SELECT * FROM countries ORDER BY name ASC"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['continent'], row['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['continent'], result['id'])
    return country

def update(country):
    sql = "UPDATE countries SET (name, continent) = (%s, %s) WHERE id = %s"
    values = [country.name, country.continent, country.id]
    print(values)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)