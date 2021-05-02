from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm
from verify_image import check_url

app = Flask(__name__)

# DebugToolbarExtension code str8 from docs
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5432/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/new', methods=['GET', 'POST'])
def new_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        if photo_url == '' or not check_url(photo_url):
            photo_url = None
        age = form.age.data
        if age == '':
            age = None
        notes = form.notes.data
        if notes == '':
            notes = None
        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')

    return render_template('new-pet-form.html', form=form)
