'''
@Time    :   2019/05/22 23:47:20
'''
__AUTHOR__ = 'xwp' 

import os
import sys

WIN = sys.platform.startswith('win')


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
    
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MySQL.@localhost/first_flask'

config = {
    'development':DevelopmentConfig
}