from flask import Flask, render_template, request

import sys, datetime, k2connect

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello There World!'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token', methods=['GET'])
def access_token():
    return render_template('token.html')


@app.route('/request_token', methods=['POST'])
def request_token():
    client_id = request.form['client-id']
    client_secret = request.form['client-secret']
    given_time = datetime.datetime.now()

    return render_template('token.html', client_id=client_id, client_secret=client_secret, given_time=given_time)


if __name__ == '__main__':
    app.run()
