from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.attraction_repository as attraction_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route("/cities")
def display_cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

# SHOW
@cities_blueprint.route("/cities/<id>", methods=["GET"])
def show_city(id):
    city = city_repository.select(id)
    attractions = attraction_repository.select_attraction_by_city(id)
    return render_template("cities/show.html", city = city, attractions = attractions)

# SHOW LIST OF VISITED CITIES
@cities_blueprint.route("/cities/visited", methods=["GET"])
def show_visited_cities():
    cities = city_repository.select_all_visited()
    return render_template("cities/visited.html", cities = cities)

# SHOW LIST OF CITIES STILL TO VISIT
@cities_blueprint.route("/cities/not_visited", methods=["GET"])



# NEW

@cities_blueprint.route("/cities/new", methods=["GET"])
def new_city():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("cities/new.html", cities = cities, countries = countries)

# CREATE

@cities_blueprint.route("/cities", methods=["POST"])
def create_city():
    name = request.form["name"]
    country_id = request.form['country']
    notes = request.form["notes"]
    visited = request.form["visited"]

    country = country_repository.select(country_id)
    city = City(name, country, notes, visited)
    city_repository.save(city)
    return redirect("/cities")

# EDIT
@cities_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_city(id):
    city = city_repository.select(id)
    countries = country_repository.select_all()
    return render_template("cities/edit.html", city = city, countries = countries)

# UPDATE
@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    name =request.form["name"]
    country_id = request.form["country_id"]
    notes = request.form["notes"]
    visited = request.form["visited"]

    country = country_repository.select(country_id)
    city = City(name, country, notes, visited, id)
    city_repository.update(city)
    return redirect(f"/cities/{id}")

# DELETE

@cities_blueprint.route("/cities/<id>/delete", methods=["GET"])
def delete_city(id):
    city_repository.delete(id)
    return redirect("/cities")