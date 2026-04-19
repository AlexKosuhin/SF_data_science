from flask import Flask, request
import datetime

app = Flask(__name__)

@app.route('/hello')
def hello_func():
    name = request.args.get('name')
    return f'hello, {name}!'

@app.route('/time')
def time():
    now = datetime.datetime.now()
    return f'{now}'


if __name__ == '__main__':
    app.run('localhost', 5000)
    