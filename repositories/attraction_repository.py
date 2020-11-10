from db.run_sql import run_sql

from models.attraction import Attraction
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository

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
    sql = "SELECT * FROM attractions" 
    # ORDER BY city.id"
    results = run_sql(sql)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['cost'], city, row['id'])
        attractions.append(attraction)
    return attractions

def select(id):
    attraction = None
    sql = "SELECT * FROM attractions WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        city = city_repository.select(result['city_id'])
        attraction = Attraction(result['name'], result['cost'], city, result['id'])
    return attraction

def select_attraction_by_city(id):
    attractions = []

    sql = "SELECT * FROM attractions WHERE city_id = %s"
    values = [id]
    results = run_sql(sql, values)

    for row in results:
        city = city_repository.select(row['city_id'])
        attraction = Attraction(row['name'], row['cost'], city, row['id'])
        attractions.append(attraction)
    return attractions

def update(attraction):
    sql = "UPDATE attractions SET (name, cost, city_id) = (%s, %s, %s) WHERE id = %s"
    values = [attraction.name, attraction.cost, attraction.city.id, attraction.id]
    print(values)
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM attractions"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM attractions WHERE id = %s"
    values = [id]
    run_sql(sql, values)