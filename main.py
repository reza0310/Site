from flask import Flask, render_template, url_for, send_from_directory

app = Flask(__name__)

@app.route('/favicon.ico')
@app.route('/univers/aube/favicon.ico')
@app.route('/univers/favicon.ico')
def favicon():
    return send_from_directory(app.root_path, 'favicon.ico', mimetype='image/vnd.microsoft.icon')

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


@app.route("/univers/aube")
def aube():
    return render_template("univers/aube.html", titre="Aube")


@app.route("/univers/aube/thulium")
def thulium():
    return render_template("univers/aube/Thulium.html", titre="Aube")


@app.route("/univers/aube/francium")
def francium():
    return render_template("univers/aube/Francium.html", titre="Aube")


@app.route("/univers/aube/hydrogene")
def hydrogene():
    return render_template("univers/aube/Hydrogene.html", titre="Aube")


@app.route("/univers/autre")
def autre():
    return render_template("univers/autre.html")


@app.route("/actualites")
def actualites():
    return render_template("actualites.html")


@app.route("/clubs")
def clubs():
    return render_template("clubs.html")


@app.route("/telechargements")
def telechargements():
    return render_template("telechargements.html")


@app.route("/outils")
def contact():
    return render_template("outils.html")

@app.route('/calcul_imc')
def calcul_imc():
    return send_from_directory(app.root_path, 'JavaScripts/calcul_imc.js', mimetype='JavaScript')


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