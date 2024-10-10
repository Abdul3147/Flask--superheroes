from random import choice as rc
from app import app
from models import db, Hero, Power, HeroPower

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        HeroPower.query.delete()
        Power.query.delete()
        Hero.query.delete()

        print("Seeding powers...")
        powers = [
            Power(name="Super Strength", description="Gives the wielder super-human strength."),
            Power(name="Flight", description="Allows the wielder to fly at supersonic speeds."),
            Power(name="Superhuman Senses", description="Gives superhuman-level senses."),
            Power(name="Elasticity", description="Gives the ability to stretch the body to extreme lengths.")
        ]
        db.session.add_all(powers)
        db.session.commit()

        print("Seeding heroes...")
        heroes = [
            Hero(name="Kamala Khan", super_name="Ms. Marvel"),
            Hero(name="Doreen Green", super_name="Squirrel Girl"),
            Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
            Hero(name="Janet Van Dyne", super_name="The Wasp"),
            Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
            Hero(name="Carol Danvers", super_name="Captain Marvel"),
            Hero(name="Jean Grey", super_name="Dark Phoenix"),
            Hero(name="Ororo Munroe", super_name="Storm"),
            Hero(name="Kitty Pryde", super_name="Shadowcat"),
            Hero(name="Elektra Natchios", super_name="Elektra"),
        ]
        db.session.add_all(heroes)
        db.session.commit()

        print("Adding powers to heroes...")
        strengths = ["Strong", "Weak", "Average"]
        for hero in heroes:
            power = rc(powers)
            hero_power = HeroPower(hero=hero, power=power, strength=rc(strengths))
            db.session.add(hero_power)

        db.session.commit()
        print("Seeding succeded!")
