'''
@Time    :   2019/05/23 00:04:47
'''
__AUTHOR__ = 'xwp' 

from flask import Blueprint

web = Blueprint('web', __name__, template_folder='templates')
auth_bp = Blueprint('auth',__name__)
admin_bp = Blueprint('admin',__name__)

from app.web import route
from app.web import admin
from app.web import auth