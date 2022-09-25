# venv = entorno virtual = para poder hacer deploy # pip install virtualenv # py -3 -m venv venv
# pip install flask dentro de scripts
# importar flask o djamgo y render template
from flask import Flask, render_template

# inicializarlo y guardar en variable app * nombre de aplicacion = app
app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something * pag ppal * def = función
@app.route('/')
def home():
    # return ("hola")
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    # return render_template("about.html")
    return ("about.html")

# Make sure this we are executing this file * if es el archivo ppal * modo debug para q se autoreinicie tipo nodemon
if __name__ == '__main__':
    app.run(debug=True)

# http://127.0.0.1:5000
# localhost:5000