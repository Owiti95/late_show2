from flask import Blueprint, jsonify
from .models import Episode, Guest, Appearance

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify(message="Welcome to The Late Show")
