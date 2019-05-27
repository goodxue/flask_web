'''
@Time    :   2019/05/19 11:32:14
'''
__AUTHOR__ = 'xwp' 

from flask import Flask
from app.models.base import db 

def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('app.settings')
    app.config.from_object('app.secure')
    register_web_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app



if __name__ == '__main__':
    app.run() 