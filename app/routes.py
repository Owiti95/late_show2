from flask import Blueprint, jsonify, request
from .models import Episode, Guest, Appearance
from app import db


main = Blueprint('main', __name__)

@main.route('/')
def home():
    return jsonify(message="Welcome to The Late Show")

#GET /episodes
@main.route('/episodes', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes])

#GET /episodes/:id
@main.route('/episodes/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get(id)
    if episode is None:
        return jsonify({"error": "Episode not found"}), 404

    appearances = [
        {
            "id": appearance.id,
            "rating": appearance.rating,
            "episode_id": appearance.episode_id,
            "guest_id": appearance.guest_id,
            "guest": {
                "id": appearance.guest.id,
                "name": appearance.guest.name,
                "occupation": appearance.guest.occupation,
            },
        }
        for appearance in episode.appearances
    ]

    return jsonify({
        "id": episode.id,
        "date": episode.date,
        "number": episode.number,
        "appearances": appearances
    })

#GET /guests
@main.route('/guests', methods=['GET'])
def get_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests])

#POST /appearances
@main.route('/appearances', methods=['POST'])
def add_appearance():
    data = request.get_json()
    if 'rating' not in data or 'episode_id' not in data or 'guest_id' not in data:
        return jsonify({"errors": ["validation errors"]}), 400

    #fetching the associated Episode and Guest
    episode = Episode.query.get(data['episode_id'])
    guest = Guest.query.get(data['guest_id'])

    if episode is None or guest is None:
        return jsonify({"errors": ["validation errors"]}), 400

    new_appearance = Appearance(
        rating=data['rating'],
        episode_id=data['episode_id'],
        guest_id=data['guest_id']
    )

    db.session.add(new_appearance)
    db.session.commit()

    return jsonify({
        "id": new_appearance.id,
        "rating": new_appearance.rating,
        "guest_id": new_appearance.guest_id,
        "episode_id": new_appearance.episode_id,
        "episode": {
            "id": episode.id,
            "date": episode.date,
            "number": episode.number
        },
        "guest": {
            "id": guest.id,
            "name": guest.name,
            "occupation": guest.occupation
        }
    }), 201