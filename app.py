from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = 'bcc9bdc83147456ebd8da8bfe5eec301'

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




if __name__ == '__main__':
    app.run(debug=True)