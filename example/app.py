import datetime
import k2connect

from flask import Flask, render_template, request

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

    k2connect.initialize(client_id, client_secret, 'https://127.0.0.1:3000/')
    token_service = k2connect.Tokens
    access_token_request = token_service.request_access_token()
    # access_token = token_service.get_access_token(access_token_request)

    return render_template('token.html', client_id=client_id, client_secret=client_secret, given_time=given_time, access_token=access_token)


if __name__ == '__main__':
    app.run()
