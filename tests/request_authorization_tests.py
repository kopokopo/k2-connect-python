from flask import Flask
from flask import request, abort
import hmac
import hashlib
import os
from request_authorization import request_authorization
from decompose_payload import pay_load_data
auth_layer = Flask(__name__)

k2_api_key = os.getenv('K2_API_TOKEN')


def gen_hmac_sig(api_key, msg):
    signature = hmac.new(api_key, msg, hashlib.sha256).hexdigest()
    return signature


def get_header_value(header_file):
    sig = header_file.get(os.getenv('k2_SERVER_SIGNATURE'))
    return sig


@auth_layer.route('/buyGoods_Transaction', methods=['POST'])
def get_data():
    if request.method == 'POST':

        # get header values
        headers = request.headers

        # get json_object
        json_object = request.json

        k2 = request_authorization(k2_api_key=k2_api_key, k2_headers=headers, k2_json_object=json_object)

        # decompose json object to get data
        decomposer = pay_load_data(k2.object_authorization(), json_object).decompose()

        # get transaction first name
        firstName = decomposer

        print(firstName)

        return 'Request Successful', 200
    else:
        abort(400)


if __name__ == '__main__':
    auth_layer.run()
