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
@attractions_blueprint.route("/attractions/<id>", methods=["GET"])
def show_attraction(id):
    attraction = attraction_repository.select(id)
    return render_template("attractions/show.html", attraction = attraction)


# NEW
@attractions_blueprint.route("/attractions/new", methods=["GET"])
def new_attraction():
    attractions = attraction_repository.select_all()
    cities = city_repository.select_all()
    return render_template("attractions/new.html", attractions = attractions, cities = cities)

# CREATE

@attractions_blueprint.route("/attractions", methods=['POST'])
def create_attraction():
    name = request.form["name"]
    cost = request.form["cost"]
    city_id = request.form["city"]

    city = city_repository.select(city_id)
    attraction = Attraction(name, cost, city)
    attraction_repository.save(attraction)
    return redirect("/attractions")


# EDIT



# UPDATE



# DELETE
@attractions_blueprint.route("/attractions/<id>/delete", methods=["GET"])
def delete_attraction(id):
    attraction_repository.delete(id)
    return redirect("/attractions")