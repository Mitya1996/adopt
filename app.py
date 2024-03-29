import os
from flask import Flask, render_template, redirect, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm
from verify_image import check_url
from werkzeug.utils import secure_filename


app = Flask(__name__)
UPLOAD_FOLDER = './static'

# DebugToolbarExtension code str8 from docs
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:myPassword@localhost:5432/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


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
        if photo_url and form.photo_file.data:
            flash('Photo Url or Photo Upload, but not both.')
            return redirect('/new')
        if photo_url == '' or not check_url(photo_url):
            photo_url = None
        if form.photo_file.data:
            f = request.files['photo_file']
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
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

    return render_template('pet-create.html', form=form)

@app.route('/<int:id>', methods=['GET', 'POST'])
def pet_read_update(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if request.method == 'GET':
        if app.config['UPLOAD_FOLDER'] in form.photo_url.data:
            form.photo_url.data = ""
    #post
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        if photo_url and form.photo_file.data:
            flash('Photo Url or Photo Upload, but not both.')
            return redirect(f'/{id}')
        if photo_url == '' or not check_url(photo_url):
            photo_url = './static/default_pet.png'
        if form.photo_file.data:
            f = request.files['photo_file']
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            photo_url = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        age = form.age.data
        if age == '':
            age = None
        notes = form.notes.data
        if notes == '':
            notes = None
        pet.name = name
        pet.species = species
        pet.photo_url = photo_url
        pet.age = age
        pet.notes = notes
        db.session.commit()
        return redirect(f'/{id}')

    return render_template('pet-read-update.html', form=form, pet=pet)