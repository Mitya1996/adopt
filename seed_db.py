from models import db, Pet

def seed_db():
    db.drop_all()
    db.create_all()


seed_db()