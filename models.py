from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""

    __tablename__ = "users"

    id = db.Column(
        db.Integer, 
        autoincrement=True, 
        primary_key=True)
    name = db.Column(
        db.Text, 
        nullable=False)
    species = db.Column(
        db.Text, 
        nullable=False)
    photo_url = db.Column(
        db.Text)
    age = db.Integer(
        db.Text)
    notes = db.Column(
        db.Text)
    available = db.Column(
        db.Boolean,
        nullable=False,
        default=True)

    def __repr__(self):
        return '<User %r>' % self.username

# Create a single model, Pet. This models a pet potentially available for adoption:

# id: auto-incrementing integer
# name: text, required
# species: text, required
# photo_url: text, optional
# age: integer, optional
# notes: text, optional
# available: true/false, required, should default to available
# While setting up the project, add the Debug Toolbar.

