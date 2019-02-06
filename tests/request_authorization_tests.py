"""FLask test for classes"""
from flask import Flask
import os
from flask import request, abort
import json
import hashlib
import hmac

app = Flask(__name__)

k2_client_secret = "d105675be1a5d34ec2da875d586b37a39c59ca5c"


def gen_hmac_sig(api_key, message):
    signature = hmac.new(api_key, message, hashlib.sha256).hexdigest()
    return signature


@app.route('/buyGoods_Transaction', methods=['POST'])
def test():
    if request.method == 'POST':
        # get request headers
        headers = request.headers
        data = request.data

        # get json file
        json_object = request.json
        if json_object and data is not None:
            if json.dumps(json_object).encode('utf8') == data:
                print("Success")
            else:
                print("epic failures")

            hash_sig = gen_hmac_sig(bytes(k2_client_secret, 'utf-8'), json.dumps(json_object).replace(" ", "").encode('utf8'))
            print(hmac.compare_digest(hash_sig, headers.get('X-KopoKopo-Signature')))

        return 'Authenticated', 200

    else:
        abort(400)


if __name__ == '__main__':
    app.run()
