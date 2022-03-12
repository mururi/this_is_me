from flask import render_template
from . import main

# Views
@main.route('/')
def index():
    title = 'This is Me'

    return render_template('index.html', title=title)