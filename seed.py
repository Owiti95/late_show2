from app import db, create_app
from app.models import Episode, Guest, Appearance

def seed_data():
    app = create_app()
    app.app_context().push()

    e1 = Episode(date="2023-01-01", number=1)
    g1 = Guest(name="Tony Owiti", occupation="Actor")
    g2 = Guest(name="Alison Onyango", occupation="Comedian")

    a1 = Appearance(rating=5, episode=e1, guest=g1)
    a2 = Appearance(rating=4, episode=e1, guest=g2)

    db.session.add_all([e1, g1, g2, a1, a2])
    db.session.commit()

if __name__ == "__main__":
    seed_data()
