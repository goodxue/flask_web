'''
@Time    :   2019/05/19 11:32:14
'''
__AUTHOR__ = 'xwp' 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

if __name__ == '__main__':
    app.run() 