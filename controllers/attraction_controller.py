from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attraction import Attraction
import repositories.attraction_repository as attraction_repository
import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

attractions_blueprint = Blueprint("attractions", __name__)

# INDEX
@attractions_blueprint.route("/attractions")
def display_attractions():
    attractions = attraction_repository.select_all()
    return render_template("attractions/index.html", attractions = attractions)


# SHOW



# NEW
# @attractions_blueprint.route("/attractions/new", methods=["GET"])

# CREATE



# EDIT



# UPDATE



# DELETE