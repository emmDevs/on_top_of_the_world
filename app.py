from flask import Flask, render_template
from db.run_sql import run_sql

from models.attraction import Attraction
from models.city import City
from models.country import Country

from controllers.country_controller import countries_blueprint
from controllers.city_controller import cities_blueprint
from controllers.attraction_controller import attractions_blueprint
import repositories.search_repository as search_repository


app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(cities_blueprint)
app.register_blueprint(attractions_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<search>')
def display_search_results(search):
    search_results = search_repository.user_search_cities(search)
    return render_template('/search.html', search_results = search_results)


# @app.route('/<search>')
# def user_search(search):
#     search_results = []
#     sql = SELECT * FROM attractions WHERE attraction.name LIKE % %s % UNION ALL SELECT * FROM cities where city.name LIKE % %s % UNION ALL SELECT * FROM countries WHERE countries.name like % %s %
#     values = [search]
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


# @app.route('/<search>')
# def user_search(search):
#     attraction = Attraction(row['name'], row['cost'], city, row['id'])
#     city = City(row['name'], country, row['notes'], row['visited'], row['id'])
#     country = Country(row['name'], row['continent'], row['id'])
#     return render_template('search.html', attraction = attraction, city = city, country=country)

if __name__ == '__main__':
    app.run(debug=True)