import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'jjhjhjhjhiui')
    DEGUG = True


class DevelopmentConfig(Config):
    DEGUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


Config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
