<<<<<<< HEAD
# k2_connect_python
A python module to connect to the Kopo Kopo application
# define app name
auth_layer = Flask(__name__)

# access credentials
K2_sig_header_ref = os.getenv('k2_SERVER_SIGNATURE')

# elements of request
post_method = 'POST'


def endpoint(req_endpoint):
    url_endpoint = "/" + req_endpoint
    return url_endpoint


def gen_hmac_sig(api_key, msg):
    signature = hmac.new(api_key, msg, hashlib.sha256).hexdigest()
    return signature
=======
# k2-connect-python
Python SDK to connect to the Kopo Kopo API
>>>>>>> k2-connect-python/master
