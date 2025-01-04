from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    birth_year = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)
    gender = db.Column(db.String(80), unique=False, nullable=False)
    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "height": self.height,
            "mass": self.mass,
            "name": self.name,
            "skin_color": self.skin_color
        }

class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    director = db.Column(db.String(80), unique=False, nullable=False)
    producer = db.Column(db.String(200), unique=False, nullable=False)
    release_date = db.Column(db.String(80), unique=False, nullable=False)
    opening_crawl = db.Column(db.String(500), unique=False, nullable=False)

    def __repr__(self):
        return f'<Film {self.title}>'

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "director": self.director,
            "producer": self.producer,
            "release_date": self.release_date,
            "opening_crawl": self.opening_crawl,
        }

class Species(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    classification = db.Column(db.String(80), unique=False, nullable=False)
    designation = db.Column(db.String(80), unique=False, nullable=False)
    average_height = db.Column(db.String(80), unique=False, nullable=False)
    average_lifespan = db.Column(db.String(80), unique=False, nullable=False)
    eye_colors = db.Column(db.String(200), unique=False, nullable=False)
    hair_colors = db.Column(db.String(200), unique=False, nullable=False)
    skin_colors = db.Column(db.String(200), unique=False, nullable=False)
    language = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f'<Species {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification": self.classification,
            "designation": self.designation,
            "average_height": self.average_height,
            "average_lifespan": self.average_lifespan,
            "eye_colors": self.eye_colors,
            "hair_colors": self.hair_colors,
            "skin_colors": self.skin_colors,
            "language": self.language
        }
    
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', backref='favorites')  
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  
    people = db.relationship('People')
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=True)
    film = db.relationship('Film')
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=True)
    species = db.relationship('Species')
    species_id = db.Column(db.Integer, db.ForeignKey('species.id'), nullable=True)

    def __repr__(self):
        return f'<Favorites {self.id}>'

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "people": self.people_id,
            "film": self.film_id,
            "species": self.species_id,
        }