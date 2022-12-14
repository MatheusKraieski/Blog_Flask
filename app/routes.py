from flask import render_template, url_for, flash, redirect
from app.models import User, Post
from app import app, bcrypt
from app.forms import RegistrationForm, LoginForm
from app import db

posts = [
    {
        'author': 'Matheus kraieski',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'Aplil 20, 2022'

    },
    {
        'author': 'José kraieski',
        'title': 'blog post 2',
        'content': 'Second post content',
        'date_posted': 'Aplil 21, 2022'

    },

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your account has been created", 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@login.com' and form.password.data == 'password':
            flash('you have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
             flash('Login Unsuccessful, please check', 'danger')
    return render_template('login.html', title='login', form=form)