from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.attraction import Attraction
import repositories.attraction_repository as attraction_repository

attractions_blueprint = Blueprint("attractions", __name__)