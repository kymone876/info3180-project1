import os


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my-super-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://project1:kkiss@localhost/project1'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://eudilppvcoxgnm:be5503240f7b5460a63ec5cd2433cef52cefafc5762909e307c524b228d0496c@ec2-52-21-252-142.compute-1.amazonaws.com:5432/dbe6vdabpc249s'
    # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOAD_FOLDER = os.environ['UPLOAD_FOLDER'] = 'uploads'


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
