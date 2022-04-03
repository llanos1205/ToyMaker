from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/version')
def version():
    return os.environ.get('FLASK_ENV')


if __name__ == '__main__':
    app.run()
