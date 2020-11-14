from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/projet")
def projet():
    return render_template("projet.html")


@app.route("/univers")
def univers():
    return render_template("univers.html")


@app.route("/actualites")
def actualites():
    return render_template("actualites.html")


@app.route("/clubs")
def clubs():
    return render_template("clubs.html")


@app.route("/telechargements")
def telechargements():
    return render_template("telechargements.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/credits")
def credits():
    return render_template("credits.html")


posts = [
    {'auteur': 'reza0310', 'titre': 'Premier post', 'contenu': 'Bienvenue sur le blog de l\'O.D.A.A.M.E. qui est plus là en tant que démo technique qu\'autre chose.', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'},
    {'auteur': 'reza0310', 'titre': 'Lorem ipsum', 'contenu': 'Lorem ipsum dolor sit amet', 'date': '14/11/2020'}
]


@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts, titre="blog")


if __name__ == '__main__':
    app.run(debug=True)