from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name",
        validators=[InputRequired()])
    species = StringField("Species",
        validators=[InputRequired()])
    photo_url = StringField("Photo Url",
        validators=[Optional()])
    age = IntegerField("Age",
        validators=[Optional()])
    notes = TextAreaField("Notes",
        validators=[Optional()])

