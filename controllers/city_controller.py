from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

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
    return render_template("cities/show.html", city = city)


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


# UPDATE