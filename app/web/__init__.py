'''
@Time    :   2019/05/23 00:04:47
'''
__AUTHOR__ = 'xwp' 

from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')

from app.web import app