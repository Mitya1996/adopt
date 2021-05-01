from models import db, Pet
from app import app

def seed_db():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    pet1 = Pet(name='Lupe', species='Dog', age=10, notes='What a good dog!', available=False)
    pet2 = Pet(name='Lucy', species='Cat', age=20, notes='RIP', available=False)
    pet3 = Pet(name='Kermy', species='Parrot', age=45, notes='Annoying')
    pet4 = Pet(name='Barbadeus', species='Armadillo', age=2, notes='Hard shell.')
    pet5 = Pet(name='Tigey', species='Tiger', notes='Rare big kitty', available=False)
    pet6 = Pet(name='Trunkus', species='Elephant', age=10, notes='Huge animal that loves to create a fountain with his nose.')
    pet7 = Pet(name='Stripe', species='Zebra', notes='Black and white stripes.', available=False)
    db.session.add_all([pet1, pet2, pet3, pet4, pet5, pet6, pet7])
    db.session.commit()

seed_db()


# Create a single model, Pet. This models a pet potentially available for adoption:

# id: auto-incrementing integer
# name: text, required
# species: text, required
# photo_url: text, optional
# age: integer, optional
# notes: text, optional
# available: true/false, required, should default to available
# While setting up the project, add the Debug Toolbar.
