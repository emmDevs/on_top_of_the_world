from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

# INDEX
@cities_blueprint.route("/cities")
def display_cities():
    cities = city_repository.select_all()
    return render_template("cities/index.html", cities = cities)

# SHOW



# NEW


# CREATE


# EDIT


# UPDATE