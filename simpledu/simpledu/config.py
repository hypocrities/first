class BaseConfig(object):
    SECRET_KEY = 'makesure to set a very secret key'

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@127.0.0.1:3306/simpledu?charset=utf8'


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

