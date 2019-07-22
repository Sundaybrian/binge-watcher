# where we will create all our view functions

from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message="Helo there"
    return render_template('index.html',message=message)

  