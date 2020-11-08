from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

# INDEX
@countries_blueprint.route("/countries")
def display_countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", countries = countries)

# SHOW
@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template("countries/show.html", country = country)

# I want to list the cities under each country - maybe I should use a separate route?
@countries_blueprint.route("/countries/<id>", methods=["GET"])
def list_cities_for_country(id):
        cities = city_repository.select_city_by_country(id)
        return render_template("countries/show.html", cities = cities)

# NEW

@ countries_blueprint.route("/countries/new", methods=["GET"])
def new_country():
    countries = country_repository.select_all()
    return render_template("/countries/new.html", countries = countries)

# CREATE

@countries_blueprint.route("/countries", methods=["POST"])
def create_country():
    name = request.form["name"]
    continent = request.form["continent"]

    country = Country(name, continent)
    country_repository.save(country)
    return redirect("/countries")    

# EDIT

@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select(id)
    return render_template("/countries/edit.html", country = country)

# UPDATE
@countries_blueprint.route("/countries/<id>/edit", methods=["GET" "POST"])
def update_country(id):
    name = request.form["name"]
    continent = request.form["continent"]

    country = Country(name, continent, id)
    country_repository.update(country)
    return redirect("/countries")


# DELETE

@countries_blueprint.route("countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")