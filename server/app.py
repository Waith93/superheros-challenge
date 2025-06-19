from flask import Flask, jsonify, request
from server.models import db, Hero, HeroPower, Power
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route('/')
    def index():
        return "<h1>Welcome to the Superheroes API!</h1>"

    @app.route('/heroes', methods=['GET'])
    def get_heroes():
        heroes = Hero.query.all()
        hero_list = [
            {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            } for hero in heroes
        ]
        return jsonify(hero_list), 200

    @app.route('/heroes/<int:id>', methods=['GET'])
    def get_hero_by_id(id):
        hero = Hero.query.filter_by(id=id).first()

        if not hero:
            return jsonify({"error": "Hero not found"}), 404

        hero_data = {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "id": hp.id,
                    "hero_id": hp.hero_id,
                    "power_id": hp.power_id,
                    "strength": hp.strength,
                    "power": {
                        "id": hp.power.id,
                        "name": hp.power.name,
                        "description": hp.power.description
                    }
                }
                for hp in hero.hero_powers
            ]
        }
        return jsonify(hero_data), 200

    @app.route('/powers', methods=['GET'])
    def get_powers():
        powers = Power.query.all()
        powers_list = [
            {
                "id": power.id,
                "name": power.name,
                "description": power.description
            } for power in powers
        ]
        return jsonify(powers_list), 200

    @app.route('/powers/<int:id>', methods=['GET'])
    def get_power_by_id(id):
        power = Power.query.filter_by(id=id).first()
        if not power:
            return jsonify({"error": "Power not found"}), 404
        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power_by_id(id):
        power = Power.query.filter_by(id=id).first()

        if not power:
            return jsonify({"error": "Power not found"}), 404

        data = request.get_json()
        description = data.get('description')

        if not description or len(description) < 20:
            return jsonify({"errors": ["validation errors"]}), 400

        power.description = description
        db.session.commit()

        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    @app.route('/hero_powers', methods=['POST'])
    def create_hero_power():
        data = request.get_json()

        strength = data.get('strength')
        hero_id = data.get('hero_id')
        power_id = data.get('power_id')

        if strength not in ['Strong', 'Weak', 'Average']:
            return jsonify({"errors": ["validation errors"]}), 400

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            return jsonify({"errors": ["validation errors"]}), 400

        hero_power = HeroPower(strength=strength, hero=hero, power=power)

        db.session.add(hero_power)
        db.session.commit()

        return jsonify({
            "id": hero_power.id,
            "hero_id": hero.id,
            "power_id": power.id,
            "strength": hero_power.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }), 201

    return app