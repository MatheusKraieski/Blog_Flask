from flask import Flask, render_template, url_for, flash, redirect
from datetime import datetime
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = 'bcc9bdc83147456ebd8da8bfe5eec301'
db = SQLAlchemy()
db.init_app(app)

with app.app_context():
    db.create_all()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String(100), nullable=False)
     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
     content = db.Column(db.Text, nullable=False)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

     def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"    


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

@app.route("/users")
def users():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return "lol"


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", 'success')
        return redirect(url_for('home'))
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


if __name__ == '__main__':
    app.run(debug=True)
