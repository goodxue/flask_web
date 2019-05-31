'''
@Time    :   2019/05/22 23:49:59
'''
__AUTHOR__ = 'xwp' 

from flask import Flask,render_template
from . import web

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/test')
def test():
    return web.send_static_file('test.html')