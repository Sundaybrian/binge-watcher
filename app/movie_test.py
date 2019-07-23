import unittest
from models import movie #from models folder import the movie.py
Movie = movie.Movie #set a local variable equal to the Movie class from the movie.py file

class MovieTest(unittest.TestCase):
    '''
    Test class to test behaviour of the movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''

        self.new_movie=Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))


if __name__=='__main__':
    unittest.main()        
