from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name")
    species = StringField("Species")
    photo_url = StringField("Photo Url")
    age = IntegerField("Age")
    notes = StringField("Notes")
