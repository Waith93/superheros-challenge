from server.models import db, Hero, Power, HeroPower
from server.app import create_app

app = create_app()

with app.app_context():

    Hero.query.delete()
    Power.query.delete()
    HeroPower.query.delete()
    
    flight = Power(name="Flight", description="Allows the user to fly freely across the sky.")
    invisibility = Power(name="Invisibility", description="Grants the power to become invisible at will.")
    strength = Power(name="Super Strength", description="Gives immense physical power and force.")

    # Create Heros
    hero1 = Hero(name="Clark Kent", super_name="Superman")
    hero2 = Hero(name="Diana Prince", super_name="Wonder Woman")
    hero3 = Hero(name="Bruce Wayne", super_name="Batman")

    # Create HeroPowers
    hp1 = HeroPower(strength="Strong", hero=hero1, power=flight)
    hp2 = HeroPower(strength="Average", hero=hero2, power=strength)
    hp3 = HeroPower(strength="Weak", hero=hero3, power=invisibility)

    # Add all to the session
    db.session.add_all([flight, invisibility, strength])
    db.session.add_all([hero1, hero2, hero3])
    db.session.add_all([hp1, hp2, hp3])

    
    db.session.commit()