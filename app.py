from flask import Flask, render_template, request
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

@app.route('/search', methods=["POST"])
def display_search_results():
    search=request.form["search"]
    search_results = search_repository.user_search_cities(search)
    return render_template('search.html', search_results = search_results)



# @app.route('/search', methods=["POST"])
# def user_search():
#     search=request.form["search"]
#     search_results = search_repository.user_search(search)
#     return render_template('search.html', search_results = search_results)

if __name__ == '__main__':
    app.run(debug=True)