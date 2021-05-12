"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from BoBay_Area import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'public/index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/login')
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Login',
        year=datetime.now().year,
        message='Please login.'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'public/contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'public/about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/map')
def map():
    """Renders the map page."""
    return render_template(
        'public/map.html',
        title='Map',
        message='Shows all boba places in the Bay Area on map'
    )

@app.route('/test')
def test():
    return "Hello, Flask!"


"""For web design purposes"""

@app.route("/jinja")
def jinja():
    my_name = "Leo"
    return render_template("public/jinja.html", my_name=my_name)