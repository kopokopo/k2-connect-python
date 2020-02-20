# k2-connect-python

k2-connect is a Python library for accessing the Kopo Kopo APIs.

# DISCLAIMER
This library is still in development. To connect to kopokopo's current api check out it's documentation on https://app.kopokopo.com/push_api

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install k2connect.

```bash
pip install k2connect
```

## Usage
### Initialization
The library is initialized once then all services maybe accessed by creating different instances for specific services.
The `BASE_URL` is a custom value and any url maybe passed provided it is secured and should only be accessible over TLS (HTTPS) and your server should have a valid certificate.
Initialization requires the following arguments:
* `base_url`
* `client_id`
* `client_secret`

```python
import os
import k2connect

CLIENT_ID = 'my_client_id'
CLIENT_SECRET = os.getenv('MY_CLIENT_SECRET')
BASE_URL = 'https://Changed_from_localhost:3000/'

#initialize the library
k2connect.initialize(BASE_URL, CLIENT_ID, CLIENT_SECRET)
```

### k2connect services
After initialization, k2connect services may be accessed by creating instances of a specific service. For instance:
```python
# create an instance of the service 
authenticator = k2connect.Tokens

# access a method provided by the service
authenticator.request_access_token()
```
One can access the following k2connect services:
- [TokensService](#token-service)
- [PayService](#pay-service)
- [ReceivePaymentsService](#receive-payments-service)
- [TransferService](#transfers-service)
- [WebhookService](#webhook-service)

#### Token service
The token service allows you to request access tokens that you will use in order to communicate with the Kopo Kopo APIs.
The token service avails the option for you to implement token refresh mechanism by providing the duration within which
the token will expire.

The `get_access_token()` and `get_token_expiry_duration()` methods each take a response object from which they extract the
token and expiry duration values.A request token and expiry duration time can be gotten as follows: 

```python
# create an instance of the token service
token_service = k2connect.Tokens

# request the access token
access_token_request = token_service.request_access_token()

# get access token
access_token = token_service.get_access_token(access_token_request)

# get expiry duration
token_expiry_duration = token_service.get_token_expiry_duration(access_token_request)
```

#### Pay service
The pay service enables you to add external entities (recipients) as destinations for payments made withe the pay service. 
It also enables you to make payments and check for a payment's status.


To add pay recipients the `add_pay_recipient()` method is used. The currently supported recipient types are `bank_account` and 
`mobile_wallet` the method then takes a set of key worded arguments required to create a recipient of either type. The accepted 
key worded arguments are as follows:


For `bank_account` recipient:  
* account_name `REQUIRED`
* account_number `REQUIRED`
* bank_branch_id `REQUIRED`
* bank_id `REQUIRED`
* name `REQURED`


For `mobile_wallet` recipient:  
* first_name `REQUIRED`
* last_name `REQUIRED`
* phone `REQUIRED`
* network `REQUIRED`


The method allows you to pass optional `email` and `phone` key worded arguments for the recipient types.

To send payments the `send_pay()` method is used. It takes the following arguments:
* bearer_token `REQUIRED`
* callback_url `REQUIRED`
* destination `REQUIRED`
* value `REQUIRED`
* currency='KES' `REQUIRED`

 
Note: the currency argument is set to `KES` as the default currency since that is the only ISO currency currently supported. It may however, 
be overridden by passing a different currency value in its place. If you do not wish to override the `KES` currency you can simply avoid 
passing it as an argument.

The pay service also enables you to check the status of a transaction by querying a URL that points to the transaction resource, using the 
`pay_transaction_status()`.


 The Resource Location URL is returned by the either of the methods.

 ```python
# create an instance of the pay service
pay_service = k2connect.Pay

# define recipient types
BANK_ACCOUNT = 'bank_account'
MOBILE_WALLET = 'mobile_wallet'

# create bank account pay recipient
bank_pay_location = pay_service.add_pay_recipient(bearer_token=BEARER_TOKEN,
                                                          recipient_type=BANK_ACCOUNT,
                                                          account_name='Jon Snow', 
                                                          account_number='12345678912',
                                                          bank_branch_id='5656565656',
                                                          bank_id='12121212',
                                                          name='Aegon Targeryan')

# create mobile wallet pay recipient
mobile_pay_location = pay_service.add_pay_recipient(bearer_token=BEARER_TOKEN,
                                                            recipient_type=MOBILE_WALLET,
                                                            first_name='Jon',
                                                            last_name='Snow',
                                                            phone='+254123456789',
                                                            network='Safaricom')
                                                                
# send pay transaction
create_pay_location = pay_service.send_pay(bearer_token=BEARER_TOKEN,
                                            callback_url='https://myawesomeapp.com/',
                                            destination='7894571548',
                                            value='2650',
                                            # optional metadata values
                                            purpose='Loan repayment',
                                            repayment_status='complete')
```

#### Receive payments service
The receive payments service allows you to create requests for payments over a specific channel and receive the payments 
to your account. You can also check the status of your payment requests and access the payment request through a URL.


In order to create a payment request, the `create_payment_request()` method is used. This method can be passed the following arguments:
* bearer_token `REQUIRED`
* callback_url `REQUIRED`
* first_name `REQUIRED`
* last_name `REQUIRED`
* payment_channel `REQUIRED`
* phone `REQUIRED`
* till_number `REQUIRED`
* value `REQUIRED`
* currency='KES' `REQUIRED`

Note: the currency argument is set to `KES` as the default currency since that is the only ISO currency currently supported. It may however, 
be overridden by passing a different currency value in its place. If you do not wish to override the `KES` currency you can simply avoid 
passing it as an argument.


The method also creates the provision for optional `email` and `phone` information to be passed in the key worded argument form, 
for instance:


`email='mycool@email.domain'`   
`phone='+254701234567`  

Furthermore, the `create_payment_payment()` allows you to add metadata information passed in the form of a maximum of 5 key worded arguments.  
To get the URL required for checking a payment request status you use the `payment_request_location()` method which takes a http response object as an argument.  

```python
import os

# get the access token
BEARER_TOKEN = os.getenv('MY_BEARER_TOKEN')

# create an instance of the receive payments service
receive_payments_service = k2connect.ReceivePayments

# create a payment request
mpesa_payment_request = receive_payments_service.create_payment_request(bearer_token=BEARER_TOKEN,
                                                                        callback_url='https://my-cool-application-callback.com',
                                                                        first_name='Jon',
                                                                        last_name='Snow',
                                                                        payment_channel='MPESA',
                                                                        phone='+254712345678',
                                                                        till_number='111111',
                                                                        value='5000',
                                                                        # metadata values
                                                                        customer_id='KLN7845J',
                                                                        notes='Purchased item: 65')

# get payment request location
mpesa_payment_location = receive_payments_service.payment_request_location(mpesa_payment_request)

# get payment request status
payment_request_status = receive_payments_service.payment_request_status(mpesa_payment_location)
```

#### Transfers service
The transfer service enables you to create verified settlement bank accounts using the `add_settlement_account()` method. The method takes the following arguments:

* bearer_token `REQUIRED`
* account_name `REQUIRED`
* account_number `REQUIRED`
* bank_ref `REQUIRED`
* bank_branch_ref `REQUIRED`


The transfer service enables you to transfer funds to pre-approved settlement accounts. To settle funds the `settle_funds()` is used. It enables you to make two types of transfer
transactions, a blind settlement and a targeted settlement. A blind transaction is made with the `destination` argument set to `None`, in the event that an ID for the destination of funds 
is provided then a targeted transfer is made to that destination. The method takes the following arguments:

* bearer_token `REQUIRED`
* transfer_value `REQUIRED`
* transfer_currency ='KES' `REQUIRED`
* transfer_destination=None `OPTIONAL`  

Note: the currency argument is set to `KES` as the default currency since that is the only ISO currency currently supported. It may however, 
be overridden by passing a different currency value in its place. If you do not wish to override the `KES` currency you can simply avoid 
passing it as an argument.


You can check a transfer transaction's status by querying the transaction resource's location 
URL. In order to get resource location, the `transfer_transaction_location()` method is used, the method takes a http response object as an argument.  
The `transfer_transaction_status()` method is then used to check a transfer transaction status.

```python
# initialize the transfer service
transfer_service = k2connect.Transfers

# create verified settlement account
settlement_account = transfer_service.add_bank_settlement_account(bearer_token=BEARER_TOKEN,
                                                             account_name='Jon Snow',
                                                             account_number='4578124578556',
                                                             bank_ref='7814548785',
                                                             bank_branch_ref='87456874464')

# settle funds (blind transfer)
transfer_transaction = transfer_service.settle_funds(bearer_token=BEARER_TOKEN,
                                                     transfer_value='26000')
                                                     
# settle funds (targeted transfer)
transfer_transaction_2 = transfer_service.settle_funds(bearer_token=BEARER_TOKEN,
                                                       transfer_destination='457126554788',
                                                       transfer_value='26000')
# get transfer transaction location
transfer_transaction_location = transfer_service.transfer_transaction_location(transfer_transaction)

# get transfer transaction status
transfer_transaction_status = transfer_service.transfer_transaction_status(transfer_transaction_location)
```

#### Webhook service
The webhook service allows you to create subscriptions to events that occur on the KopoKopo application. The `create_subscription()` method is used, 
it takes the following arguments:

* bearer_token `REQUIRED`
* event_type `REQUIRED`
* webhook_endpoint `REQUIRED`
* webhook_secret `REQUIRED`


Currently the following events are supported:
* b2b_transaction_received
* buygoods_transaction_received
* buygoods_transaction_reversed
* merchant_to_merchant_transaction_received
* settlement_transfer_completed
* customer_created

```python
import os

# initialize webhook service
webhook_service = k2connect.Webhooks

# define a webhook secret
WEBHOOK_SECRET = os.getenv('MY_WEBHOOK_SECRET')

# create webhook subscription
customer_created_subscription = webhook_service.create_subscription(bearer_token=BEARER_TOKEN,
                                                                    event_type='customer_created',
                                                                    webhook_endpoint='https://myawesomeapplication.com/webhooks/customer_created',
                                                                    webhook_secret=WEBHOOK_SECRET)
```

#### Result processor 
Results (inclusive of webhook results and results posted to callback URLs asynchronously) sent from KopoKopo have to be processed before payloads can 
be accessed. The result processor can be used to accomplish this using the `process()` method.

```python
# initialize result handler
result_handler = k2connect.ResultHandler

# process result 
processed_payload = result_handler.process(some_result)
```

#### Payload decomposer
Once a result is processed an a payload has been returned, it can be decomposed into its constituent result data using the payload decomposer.
The payload decomposer achieves this using the `decompose()` method.

```python
from k2connect import payload_decomposer

# decompose a payload
decomposer = payload_decomposer.decompose(processed_payload)

# get first name
first_name = decomposer.first_name
```

### Author
This library was written by [PhilipWafula](https://github.com/PhilipWafula)

### Contributing
Bug reports and pull requests are welcome. Feel free raise issues on our [issues tracker](https://github.com/kopokopo/k2-connect-python/issues)

### License
k2connect-python is [MIT](https://github.com/kopokopo/k2-connect-python/blob/master/LICENSE) Licensed.

### Changelog
