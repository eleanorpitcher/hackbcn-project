from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from levelaccess.api import get_image, get_coordinates

app = Flask("levelaccess")
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///places.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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


@app.route('/')
def home():
    return "Hello, World!"


@app.route('/images/<query>')
def images(query):
    images = get_image(query)
    return images


@app.route('/places', methods=['GET'])
def get_places():
    places = Place.query.all()
    return jsonify([place.to_dict() for place in places])


@app.route('/place/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if place is None:
        abort(404, description="Place not found")
    return jsonify(place.to_dict())


@app.route('/placeinfo/<query>', methods=['GET'])
def get_placeinfo(query):
    location = get_coordinates(query)
    return jsonify(location.raw)


@app.route('/add_place/<query>', methods=['GET'])
def add_place(query):
    # Example route to add a new place
    # data = request.json
    location = get_coordinates(query)
    data = location.raw
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
    return jsonify({"message": "Place added successfully", "place": new_place.to_dict()}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
