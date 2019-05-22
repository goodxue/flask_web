'''
@Time    :   2019/05/22 23:55:47
'''
__AUTHOR__ = 'xwp' 

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)