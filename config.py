#where we will store our app configurations
import os

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_BASE_URL='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY= os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    

class ProdConfig(Config):
    '''
    Production configuration class

    Args:
        Config:The parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuraton class

    Args:
        Config:The parent configuration class with general configurations settings
    '''
    DEBUG = True #enables debug mode in our application
    

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}        