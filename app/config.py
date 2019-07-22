#where we will store our app configurations

class Config:
    '''
    General configuration parent class
    '''
    pass

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
    
        