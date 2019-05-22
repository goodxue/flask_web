'''
@Time    :   2019/05/19 11:32:14
'''
__AUTHOR__ = 'xwp' 

from flask import Flask

def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object('app.settings')
    app.config.from_object('app.secure')
    register_web_blueprint(app)
    return app



if __name__ == '__main__':
    app.run() 