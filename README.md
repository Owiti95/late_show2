# Late Show API

This is a Flask-based RESTful API for managing episodes and guest appearances on a fictional late-night show. The API allows you to retrieve information about episodes and guests, as well as create new appearances by guests on specific episodes.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Validations](#validations)
- [Contributing](#contributing)

## Technologies Used

- Python 3.8+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLAlchemy
- SQLite

## Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   cd late_show
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:

   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the environment variables:

   Create a `.env` file in the project root and add the following:

   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   SQLALCHEMY_DATABASE_URI=postgresql://username:password@localhost/lateshow
   ```

6. Initialize the database:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

7. Seed the database (optional):

   You can create a `seed.py` file to populate the database with initial data:


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



## Usage

To run the API locally, use the following command:

```bash
flask run
```

The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

### 1. Get all episodes

- **Endpoint**: `GET /episodes`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "date": "10/1/24",
      "number": 1
    },
    {
      "id": 2,
      "date": "10/2/24",
      "number": 2
    }
  ]
  ```

### 2. Get episode by ID

- **Endpoint**: `GET /episodes/:id`
- **Response (if episode exists)**:
  ```json
  {
    "id": 1,
    "date": "10/1/24",
    "number": 1,
    "appearances": [
      {
        "episode_id": 1,
        "guest": {
          "id": 1,
          "name": "Michael Maina",
          "occupation": "actor"
        },
        "guest_id": 1,
        "id": 1,
        "rating": 4
      }
    ]
  }
  ```

- **Response (if episode does not exist)**:
  ```json
  {
    "error": "Episode not found"
  }
  ```

### 3. Get all guests

- **Endpoint**: `GET /guests`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "name": "Michael Maina",
      "occupation": "actor"
    },
    {
      "id": 2,
      "name": "Sandra Sanaipei",
      "occupation": "Comedian"
    }
  ]
  ```

### 4. Create a new appearance

- **Endpoint**: `POST /appearances`
- **Request Body**:
  ```json
  {
    "rating": 5,
    "episode_id": 1,
    "guest_id": 2
  }
  ```

- **Response (on success)**:
  ```json
  {
    "id": 162,
    "rating": 5,
    "guest_id": 3,
    "episode_id": 2,
    "episode": {
      "date": "1/12/99",
      "id": 2,
      "number": 2
    },
    "guest": {
      "id": 3,
      "name": "Tracey Ullman",
      "occupation": "television actress"
    }
  }
  ```

- **Response (on failure)**:
  ```json
  {
    "errors": ["validation errors"]
  }
  ```

## Models

### Episode

- `id`: Integer, primary key
- `date`: String, date of the episode
- `number`: Integer, episode number

### Guest

- `id`: Integer, primary key
- `name`: String, guest's name
- `occupation`: String, guest's occupation

### Appearance

- `id`: Integer, primary key
- `rating`: Integer, rating of the appearance (1-5)
- `episode_id`: Integer, foreign key to `Episode`
- `guest_id`: Integer, foreign key to `Guest`

## Validations

- The `rating` in the `Appearance` model must be between 1 and 5 (inclusive).

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.
