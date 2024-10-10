from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tool
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    """Return a string indicating that the API is live."""
    return '''
        <h1>Superheroes API</h1>
        <p>Welcome to the Superheroes API! Navigate the routes to interact with heroes and their powers.</p>
    '''

@app.route('/heroes', methods=['GET'])
def get_heroes():
    """Return a list of all heroes."""
    heroes = Hero.query.all()
    return jsonify([hero.to_dict(rules=('-hero_powers',)) for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def hero_by_id(id):
    """Return a specific hero by their ID."""
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'error': 'Hero not found'}), 404
    return jsonify(hero.to_dict())

@app.route('/powers', methods=['GET'])
def get_powers():
    """Return a list of all powers."""
    powers = Power.query.all()
    return jsonify([power.to_dict(rules=('-hero_powers',)) for power in powers])

@app.route('/powers/<int:id>', methods=['GET', 'PATCH'])
def get_or_update_power(id):
    """Get a power by its ID, or update a power's details."""
    power = Power.query.get(id)
    if not power:
        return jsonify({'error': 'Power not found'}), 404

    if request.method == 'PATCH':
        description = request.json.get('description')
        if description and len(description) >= 20:  # Validate description length
            power.description = description
            db.session.commit()
            return jsonify(power.to_dict(rules=('-hero_powers',)))
        else:
            return jsonify({'errors': ['Description must be at least 20 characters long.']}), 400

    return jsonify(power.to_dict(rules=('-hero_powers',)))

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    """Create a new hero-power relationship."""
    data = request.json
    try:
        new_hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(new_hero_power)
        db.session.commit()

        return jsonify(new_hero_power.to_dict()), 201
    except Exception as e:
        return jsonify({'error': 'Validation errors', 'details': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
