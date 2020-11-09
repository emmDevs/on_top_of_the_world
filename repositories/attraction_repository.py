from db.run_sql import run_sql

from models.attraction import Attraction
from models.city import City
from models.country import Country

def save(attraction):
    sql = "INSERT INTO attractions(name, cost, city_id) VALUES (%s, %s, %s) RETURNING id"
    values = [attraction.name, attraction.cost, attraction.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    attraction.id = id
    return attraction

def select_all():
    attractions = []
# I WANT TO ORDER THE ATTRACTIONS BY CITY
    sql = "SELECT * FROM attractions ORDER BY name ASC" 
    # ORDER BY city.id"
    results = run_sql(sql)

    for row in results:
        attraction = Attraction(row['name'], row['cost'], row['city_id'], row['id'])
        attractions.append(attraction)
    return attractions

def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        attraction = Attraction(result['name'], result['cost'], result['city'], result['id'])
    return attraction

def select_attraction_by_city(city):
    attractions = []

    sql = "SELECT * FROM attractions WHERE city_id = %s"
    values = [city.id]
    results = run_sql(sql, values)

    for row in results:
        attraction = Attraction(row['name'], row['cost'], row['city'], row['id'])
        attractions.append(attraction)
    return attractions

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)