from flask import Flask, jsonify, request, abort
from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from levelaccess.api import get_mapillary_images, get_coordinates

app = Flask("levelaccess")
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///places.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    lat = db.Column(db.Float(), nullable=False)
    lon = db.Column(db.Float(), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    picture_url = db.Column(db.String(200))

    def __repr__(self):
        return f'<Place {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'lat': self.lat,
            'lon': self.lon,
            'type': self.type,
            'picture_url': self.picture_url
        }

# Create the database tables
with app.app_context():
    db.create_all()

def add_place(data):
    new_place = Place(
        name=data['name'],
        address=data['display_name'],
        lat=data['lat'],
        lon=data['lon'],
        type=data['type'],
        # thumbnail=data.get('thumbnail')  # picture_url is optional
    )
    db.session.add(new_place)
    db.session.commit()


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/images/<place_id>')
@cache.cached(timeout=300, key_prefix='images')  # Cache for 300 seconds (5 minutes)
def images(place_id):
    place = Place.query.get(place_id)
    if place is None:
        abort("Place not found")
    lat = place.lat
    lon = place.lon
    images = get_mapillary_images(lat, lon)
    return jsonify(images)


@cache.cached(timeout=300)  # Cache for 300 seconds (5 minutes)
@app.route('/places', methods=['GET'])
def get_places():
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places])


@cache.cached(timeout=300, key_prefix='place')  # Cache for 300 seconds (5 minutes)
@app.route('/place/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    return jsonify(place.to_dict())


@cache.cached(timeout=300, key_prefix='search')  # Cache for 300 seconds (5 minutes)
@app.route('/search/<query>', methods=['GET'])
def search(query):
    location = get_coordinates(query)
    data = location.raw
    existing = Place.query.filter_by(name=data['name']).first()
    if existing:
        return existing.to_dict()
    new_place = add_place(location.raw)
    return jsonify(new_place.to_dict())


@app.route('/add_place/<query>', methods=['GET'])
def add_place(query):
    location = get_coordinates(query)
    new_place = add_place(location.raw)
    return jsonify({"message": "Place added successfully", "place": new_place.to_dict()}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
