# k2-connect-python

k2-connect is a Python library for accessing the Kopo Kopo API.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install k2-connect
```

## Usage
### Receiving webhooks (Flask Implementation)

```python
# please store your client secret securely
k2_client_secret = os.getenv('K2_CLIENT_SECRET')

#import k2-connect modules
from k2client.request_authorization import RequestAuthorization
from k2client.decompose_payload import PayLoadData

# define path to your endpoint for your flask app
@app.route('/buyGoods_Transaction', methods=['POST'])

    # check request method
    if request.method == 'POST':
        # collect json body
        json_body = request.json

        # collect message body (bytes)
        message_body = request.data

        # collect headers
        headers = request.headers

        # pass parameters to validate the post request
        my_request = RequestAuthorization(
            client_secret=k2_client_secret,
            k2_json_object=json_body,
            k2_message_body=message_body,
            k2_headers=headers
            ).authorize()

        # decompose your request
        decomposer = PayLoadData(my_request).decompose()

        # get transaction details
        first_name = decomposer.sender_first_name
        
        print("First Name: ", first_name)
```
The expected output is:
```
First Name: JOHN DOE
```