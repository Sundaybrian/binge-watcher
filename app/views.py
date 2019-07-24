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
    upcoming_movie=get_movies('upcoming')
    now_showing_movie=get_movies('now_playing')


    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html',popular=popular_movies,
    upcoming=upcoming_movie,
    now_showing=now_showing_movie,
    title=title)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template("movie.html",id=movie_id)  