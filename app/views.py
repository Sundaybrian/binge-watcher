# where we will create all our view functions

from flask import render_template
from app import app
from .request import get_movies

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting popular movie

    popular_movies = get_movies('popular')
    print(popular_movies)


    title = 'Home - Welcome to The best Movie Review Website Online'
    message="Helo there"
    return render_template('index.html',popular=popular_movies,title=title)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template("movie.html",id=movie_id)  