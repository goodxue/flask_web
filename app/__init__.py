'''
@Time    :   2019/05/19 11:32:14
'''
__AUTHOR__ = 'xwp' 
import os
from flask import Flask,render_template,request
from app.extensions import db 
from app.extensions import bootstrap,db,login_manager,csrf,moment
from app.settings import config
import click

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

def register_logging(app):
    pass


def register_web_blueprint(app):
    from app.web import web
    app.register_blueprint(web)

def register_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    csrf.init_app(app)

def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG','development')

    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config.from_object('app.secure')

    register_web_blueprint(app)
    register_extensions(app)
    register_commands(app)

    #db.create_all()
    return app


def register_commands(app):
    @app.cli.command()
    @click.option('--drop',is_flag=True,help='Create after Drop.')
    def initdb(drop):
        if drop:
            click.confirm('This operation will delete the database, do you want to continue?', abort=True)
            db.drop_all()
            click.echo('Drop tables!')
        db.create_all()
        click.echo('Initialized database...')
    
    @app.cli.command()
    @click.option('--username',prompt=True,help='The username used to login.')
    @click.option('--password', prompt=True, hide_input=True,
                  confirmation_prompt=True, help='The password used to login.')
    def init(username, password):
        """Building Bluelog, just for you."""

        click.echo('Initializing the database...')
        db.create_all()

        admin = Admin.query.first()
        if admin is not None:
            click.echo('The administrator already exists, updating...')
            admin.username = username
            admin.set_password(password)
        else:
            click.echo('Creating the temporary administrator account...')
            admin = Admin(
                username=username,
                blog_title='Bluelog',
                blog_sub_title="No, I'm the real thing.",
                name='Admin',
                about='Anything about you.'
            )
            admin.set_password(password)
            db.session.add(admin)

        category = Category.query.first()
        if category is None:
            click.echo('Creating the default category...')
            category = Category(name='Default')
            db.session.add(category)

        db.session.commit()
        click.echo('Done.')

    @app.cli.command()
    @click.option('--category', default=10, help='Quantity of categories, default is 10.')
    @click.option('--post', default=50, help='Quantity of posts, default is 50.')
    @click.option('--comment', default=500, help='Quantity of comments, default is 500.')
    def forge(category, post, comment):
        """Generate fake data."""
        from app.vdata.vdata import fake_admin, fake_categories, fake_posts, fake_comments
        db.drop_all()
        db.create_all()

        click.echo('Generating the administrator...')
        fake_admin()

        click.echo('Generating %d categories...' % category)
        fake_categories(category)

        click.echo('Generating %d posts...' % post)
        fake_posts(post)

        click.echo('Generating %d comments...' % comment)
        fake_comments(comment)
        click.echo('Done.')

if __name__ == '__main__':
    app.run() 