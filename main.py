from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

posts = [
    {'auteur': 'reza0310', 'titre': 'Premier post', 'contenu': 'Bienvenue sur le blog de l\'O.D.A.A.M.E. qui est plus là en tant que démo technique qu\'autre chose.'}
]
@app.route("/blog")
def about():
    return render_template("blog.html")


if __name__ == '__main__':
    app.run(debug=True)