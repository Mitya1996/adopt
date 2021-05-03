from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, AnyOf, Regexp
from flask_wtf.file import FileField, FileAllowed

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Name",
        validators=[InputRequired()])
    species = SelectField("Species",
        choices=["cat", "dog", "porcupine"],
        validators=[InputRequired()])
    photo_url = StringField("Photo Url",
        validators=[Optional(), URL()])
    photo_file = FileField("Upload Photo",
        validators=[Optional(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp'], 'Must be a valid image.')])
    age = IntegerField("Age",
        validators=[Optional(), NumberRange(min=1, max=30)])
    notes = TextAreaField("Notes",
        validators=[Optional()])

