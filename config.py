"""Set up environment specific configurations"""
import os
class Config():
    '''Parent configuration class'''
    """Parent configuration class"""
    DEBUG = False
class Development(Config):
    '''Configuration for development environment'''
    DEBUG = True
    """Configuration for development environment"""
class Testing(Config):
    '''Configuration for testing environment'''
    """Configuration for testing environment"""
    DEBUG = True
class Production(Config):
    '''Configuration for production environment'''
    """Configuration for production environment"""
    DEBUG = False