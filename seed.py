from app import create_app, db
from app.models import Episode, Guest, Appearance

app = create_app()

def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()

        episode1 = Episode(date="10/1/24", number=1)
        episode2 = Episode(date="10/2/24", number=2)
        episode3 = Episode(date="10/3/24", number=3)

        guest1 = Guest(name="Michael Maina", occupation="Actor")
        guest2 = Guest(name="Sandra sanaipei", occupation="Comedian")
        guest3 = Guest(name="Tracey Tarrus", occupation="actress")

        db.session.add_all([episode1, episode2, episode3])
        db.session.add_all([guest1, guest2, guest3])

        appearance1 = Appearance(rating=4, episode=episode1, guest=guest1)
        appearance2 = Appearance(rating=5, episode=episode1, guest=guest2)
        appearance3 = Appearance(rating=3, episode=episode2, guest=guest3)
        appearance4 = Appearance(rating=4, episode=episode2, guest=guest1)
        appearance5 = Appearance(rating=5, episode=episode3, guest=guest2)

        db.session.add_all([appearance1, appearance2, appearance3, appearance4, appearance5])

        db.session.commit()

if __name__ == "__main__":
    seed_data()
