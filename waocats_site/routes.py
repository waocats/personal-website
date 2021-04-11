from flask import render_template, url_for
from waocats_site import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.jinja2')

@app.route('/projects')
def projects():
    return render_template('projects.jinja2')

@app.route('/about')
def about():
    return render_template('about.jinja2')

@app.route('/contact')
def contact():
    return render_template('contact.jinja2')