import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://euwhknbefserry:3b2312529bb6f9b8996b4fa6b41ba5880d0c5ade799ca3ca049f8a3d40bd6fc7@ec2-18-214-208-89.compute-1.amazonaws.com:5432/dd79o9squst6hq'
    #'postgresql://project1:kkiss@localhost/project1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER'] = 'uploads' 

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False



