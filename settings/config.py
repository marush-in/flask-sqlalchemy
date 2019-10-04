import os


class DevelopmentConfig:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:////db/test.db'


Config = DevelopmentConfig