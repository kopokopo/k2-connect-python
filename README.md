from example.app import access_tokenfrom example.app import access_tokenfrom example.app import send_moneyfrom example.app import access_tokenfrom example.app import access_tokenfrom
example.app import access_tokenfrom example.app import send_money

# k2-connect-python

[![PyPI](https://img.shields.io/pypi/v/k2-connect?style=for-the-badge)](https://pypi.org/project/k2-connect/)

k2-connect is a Python library for accessing the Kopo Kopo APIs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install k2connect.

```bash
pip3 install k2-connect
```

## Usage

### Initialization

The library is initialized once then all services maybe accessed by creating different instances for specific services.
The `BASE_URL` is a custom value and any url maybe passed provided it is secured and should only be accessible over
TLS (HTTPS) and your server should have a valid certificate.
Initialization requires the following arguments:

* `base_url`
* `client_id`
* `client_secret`

```python
import os
import k2connect

CLIENT_ID = 'MY_CLIENT_ID'
CLIENT_SECRET = 'MY_CLIENT_SECRET'
BASE_URL = 'https://sandbox.kopokopo.com/'

# initialize the library
k2connect.initialize(CLIENT_ID, CLIENT_SECRET, BASE_URL)
```

### k2connect services

After initialization, k2connect services may be accessed by creating instances of a specific service. For instance:

```python
# creating an instance of the service 
tokens_service = k2connect.Tokens

# accessing a service method
tokens_service.request_access_token()
```

One can access the following k2connect services:

- [TokensService](#token-service)
- [SendMoneyService](#send-money-service)
- [StkPushService](#stk-push-service)
- [TransferAccountService](#transfer-account-service)
- [ReceivePaymentsService](#receive-payments-service)
- [TransferService](#transfers-service)
- [WebhookService](#webhook-service)
- [NotificationService](#notification-service)
- [PollingService](#polling-service)

#### Token service

The token service allows you to request access tokens that you will use in order to communicate with the Kopo Kopo APIs.
The token service avails the option for you to implement token refresh mechanism by providing the duration within which
the token will expire.

The `get_access_token()` and `get_token_expiry_duration()` methods each take a response object from which they extract
the
token and expiry duration values.A request token and expiry duration time can be gotten as follows:

```python
# create an instance of the token service
token_service = k2connect.Tokens

# requesting the access token
access_token_request = token_service.request_access_token()

# get access token
access_token = token_service.get_access_token(access_token_request)

# get expiry duration
token_expiry_duration = token_service.get_token_expiry_duration(access_token_request)
```

### Send money service

First initialize the `SendMoney` service with the access token generated from the previous step

```python
import k2connect

send_money_service = k2connect.SendMoney(access_token=access_token)
```

Creating an outgoing payment e.g. to an M-PESA phone

```python
send_money_request = {
    "destinations": [
        {
            "type": "mobile_wallet",
            "nickname": "John Doe",
            "phone_number": "254700000000",
            "network": "Safaricom",
            "amount": 200,
            "description": "Lunch",
            "favourite": False
        }
    ],
    "callback_url": 'MY_CALLBACK_URL',
    "source_identifier": None,
    "currency": "KES"
}
send_money_service.create_payment(send_money_request)
```

The following arguments should be passed within a request:

- destinations (list of destinations) `REQUIRED`
- currency `KES` is the supported currency
- source_identifier
- callback_url `REQUIRED`

The hash structure within the destinations array:

Send to **External Mobile Recipient**

- type: 'mobile_wallet' `REQUIRED`
- phone_number `REQUIRED`
- amount `REQUIRED`
- description `REQUIRED`
- network `REQUIRED`
- first_name `OPTIONAL`
- last_name `OPTIONAL`
- nickname `OPTIONAL`

Send to **External Bank account Recipient**

- type: 'bank_account' `REQUIRED`
- account_name `REQUIRED`
- account_number `REQUIRED`
- amount `REQUIRED`
- description `REQUIRED`
- bank_branch_ref `REQUIRED`
- nickname `OPTIONAL`

Send to **External Paybill Recipient**

- type: 'paybill' `REQUIRED`
- paybill_number `REQUIRED`
- paybill_account_number `REQUIRED`
- paybill_name `OPTIONAL`
- description `REQUIRED`
- nickname `OPTIONAL`

Send to **External Till Recipient**

- type: 'till' `REQUIRED`
- till_number `REQUIRED`
- till_name `OPTIONAL`
- description `REQUIRED`
- nickname `OPTIONAL`

Send to **My Mobile Phone**

- type: 'merchant_wallet' `REQUIRED`
- reference `REQUIRED`
- amount `REQUIRED`

Send to **My Bank account**

- type: 'merchant_bank_account' `REQUIRED`
- reference `REQUIRED`
- amount `REQUIRED`

A successful response is returned with the URL of the payment resource in the HTTP `location` header.

#### Query SendMoney Request Status

To query the status of the outgoing payment request:

    send_money_service.query_resource(send_money.payments_location_url)

To query the most recent status of an outgoing payment request:

    send_money_service.query_status

A HTTP Response will be returned in a JSON Payload, accessible with the k2_response_body variable.

Code example of send money to an external recipient;

```python
```

Code example of send money to a transfer account;

```python
```

#### Receive payments service

The receive payments service allows you to create requests for incoming payments over a specific channel and receive the
payments
to your account. You can also check the status of your payment requests and access the payment request through a URL.

In order to create a payment request, the `create_payment_request()` method is used. This method can be passed the
following arguments:

* bearer_token `REQUIRED`
* callback_url `REQUIRED`
* first_name `REQUIRED`
* last_name `REQUIRED`
* payment_channel `REQUIRED`
* phone `REQUIRED`
* till_number `REQUIRED`
* value `REQUIRED`
* currency='KES' `REQUIRED`
* metadata `OPTIONAL`. Maximum 5 dictionaries/hashes/key-value pairs.

Note: the currency argument is set to `KES` as the default currency since that is the only ISO currency currently
supported. It may however,
be overridden by passing a different currency value in its place. If you do not wish to override the `KES` currency you
can simply avoid
passing it as an argument.

The method also creates the provision for optional `email` information to be passed in the key worded argument form,
for instance:

`email='mycool@email.domain'`

Furthermore, the `create_payment_request()` allows you to add metadata information passed in the form of a maximum of 5
key worded arguments.  
The URL required for checking a payment request status is returned by default with the `create_payment_request` method.

```python
import os

# get the access token
BEARER_TOKEN = os.getenv('MY_BEARER_TOKEN')

# create an instance of the receive payments service
receive_payments_service = k2connect.ReceivePayments

# create a payment request
request_payload = {
    "access_token": 'ACCESS_TOKEN',
    "callback_url": "https://webhook.site/52fd1913-778e-4ee1-bdc4-74517abb758d",
    "first_name": "python_first_name",
    "last_name": "python_last_name",
    "email": "daivd.j.kariuki@gmail.com",
    "payment_channel": "MPESA",
    "phone_number": "+254911222536",
    "till_number": "K112233",
    "amount": "10",
    "metadata": {"hey": 'there', "mister": 'angelo'}
}
mpesa_payment_location = receive_payments_service.create_payment_request(request_payload)

# get payment request status
payment_request_status = receive_payments_service.payment_request_status(access_token, mpesa_payment_location)
```

#### Transfers service

The transfer service enables you to create verified transfer accounts for both mobile and bank accounts with respective
`add_transfer_account()` methods. The method takes the following arguments:

Common for both:

* bearer_token `REQUIRED`

For `add_bank_settlement_account`:

* type `REQUIRED`
* account_name `REQUIRED`
* account_number `REQUIRED`
* bank_branch_ref `REQUIRED`
* settlement_method `REQUIRED` either `RTS` or `EFT`
* nickname `OPTIONAL`

For `add_mobile_wallet_settlement_account` recipient:

* type `REQUIRED`
* first_name `REQUIRED`
* last_name `REQUIRED`
* phone_number `REQUIRED`
* email `OPTIONAL`
* network: `REQUIRED` supported networks are `Safaricom`

The transfer service enables you to transfer funds to these pre-approved settlement accounts. To settle funds the
`settle_funds()` is used. It enables you to make two types of transfer
transactions, a blind settlement and a targeted settlement. A blind transaction is made with the `destination` argument
set to `None`, in the event that an ID for the destination of funds
is provided then a targeted transfer is made to that destination. The method takes the following arguments:

* bearer_token `REQUIRED`
* transfer_value `REQUIRED`
* transfer_currency = 'KES' `REQUIRED`
* destination_type `OPTIONAL`
* destination_reference `OPTIONAL`

Note: the currency argument is set to `KES` as the default currency since that is the only ISO currency currently
supported. It may however,
be overridden by passing a different currency value in its place. If you do not wish to override the `KES` currency you
can simply avoid
passing it as an argument.

You can check a transfer transaction's status by querying the transaction resource's location
URL which is returned by the `settle_funds` method by default.  
The `transfer_transaction_status()` method is then used to check a transfer transaction status.

```python
# initialize the transfer service
import k2connect

transfer_service = k2connect.Transfers

# create verified settlement bank account
request_payload = {
    "settlement_method": 'RTS',
    "account_name": 'py_sdk_account_name',
    "account_number": 'py_sdk_account_number',
    "bank_branch_ref": '633aa26c-7b7c-4091-ae28-96c0687cf886'
}
settlement_account = transfer_service.add_bank_settlement_account(request_payload)
# create verified settlement mobile account
request_payload = {
    "first_name": 'py_sdk_first_name',
    "last_name": 'py_sdk_last_name',
    "phone_number": '+254911222538',
    "network": 'Safaricom'
}
settlement_account = transfer_service.add_mobile_wallet_settlement_account(request_payload)

# settle funds (blind transfer)
request_payload = {
    "callback_url": 'url',
    "value": '10',
}
transfer_transaction = transfer_service.settle_funds(request_payload)

# settle funds (targeted transfer to a merchant_wallet)
request_payload = {
    "access_token": 'ACCESS_TOKEN',
    "destination_type": 'merchant_bank_account',
    "destination_reference": '87bbfdcf-fb59-4d8e-b039-b85b97015a7e',
    "callback_url": 'https://webhook.site/52fd1913-778e-4ee1-bdc4-74517abb758d',
    "value": '10',
}
transfer_transaction_mobile_location = transfer_service.settle_funds(request_payload)

# settle funds (targeted transfer to a merchant_wallet)
request_payload = {
    "destination_type": 'merchant_wallet',
    "destination_reference": 'eba238ae-e03f-46f6-aed5-db357fb00f9c',
    "callback_url": 'https://webhook.site/52fd1913-778e-4ee1-bdc4-74517abb758d',
    "value": '10',
}
transfer_transaction_bank_location = transfer_service.settle_funds(request_payload)

# get transfer transaction status
transfer_transaction_status = transfer_service.transfer_transaction_status(access_token,
                                                                           transfer_transaction_mobile_location or transfer_transaction_bank_location)
```

##### The destination_reference number corresponding to a settlement account must exist before you can settle_funds to it.

#### Webhook subscription service

The webhook service allows you to create subscriptions to events that occur on the KopoKopo application. The
`create_subscription()` method is used,
it takes the following arguments:

* event_type `REQUIRED`
* webhook_endpoint `REQUIRED`
* client_secret `REQUIRED`

The following events are supported:

* b2b_transaction_received
* buygoods_transaction_received
* buygoods_transaction_reversed
* m2m_transaction_received
* settlement_transfer_completed
* customer_created

```python
import os

# initialize service
webhook_service = k2connect.Webhooks

request_payload = {
    "event_type": 'buygoods_transaction_received',
    "webhook_endpoint": 'https://webhook.site/52fd1913-778e-4ee1-bdc4-74517abb758d',
    "scope": 'till',
    "scope_reference": '112233'
}

# create webhook subscription
customer_created_subscription = webhook_service.create_subscription(request_payload)
```

#### Notification service

This service allows you to send custom sms messages to successful buy-goods transactions received that occurred on the
Kopo Kopo.
It takes the following arguments:

* bearer_token `REQUIRED`
* webhookEventReference: The webhook event reference for a buygoods_transaction_received webhook. `REQUIRED`
* message: The message to be sent `REQUIRED`
* callbackUrl: Url that the result will be posted to `REQUIRED`

Note: A buygoods_transaction_received webhook subscription must have been created, with its subsequent webhook event in
place.

You can check an SMS notification request's status by querying the requests' location
URL which is returned by the `send_transaction_sms_notification` method by default.  
The `transaction_notification_status()` method is used to check an SMS notification request status.

```python
import os

# initialize notification service
notification_service = k2connect.Notifications

# create transaction sms notifications
request_payload = {
    "access_token": 'ACCESS_TOKEN',
    "callback_url": 'callback_url',
    "webhook_event_reference": "d81312b9-4c0e-4347-971f-c3d5b14bdbe4",
    "message": 'Alleluia',
}
notification_resource_location_url = notification_service.send_transaction_sms_notification(request_payload)

# get request status
request_status = notification_service.transaction_notification_status(access_token, notification_resource_location_url)
```

#### Polling service

This service allows you to poll transactions received on the Kopo Kopo system within a certain time range, and either a
company or a specific till.
It takes the following arguments:

* bearer_token `REQUIRED`
* fromTime: The starting time of the polling request `REQUIRED`
* toTime: The end time of the polling request `REQUIRED`
* scope: The scope of the polling request `REQUIRED`
* scopeReference: The scope reference `REQUIRED for the 'till' scope`
* callbackUrl: Url that the result will be posted to `REQUIRED`

You can check a polling request's status by querying the requests' location
URL which is returned by the `create_polling_request` method by default.  
The `polling_request_status()` method is used to check an polling request status.

```python
import os

# initialize service
polling_service = k2connect.Polling(access_token=access_token)

# initiating a polling request
request_payload = {
    "scope": "till",
    "scope_reference": "112233",
    "from_time": "2021-07-09T08:50:22+03:00",
    "to_time": "2021-07-10T18:00:22+03:00",
    "callback_url": "callback_url",
}
polling_resource_location_url = polling_service.initiate_polling_request(request_payload)

# get request status
request_status = polling_service.polling_request_status(polling_resource_location_url)
```

For more information, please
read [Transaction Notification Docs](https://api-docs.kopokopo.com/#transaction-sms-notifications)

#### Result processor

Results (inclusive of webhook results and results posted to callback URLs asynchronously) sent from KopoKopo have to be
processed before payloads can
be accessed. The result processor can be used to accomplish this using the `process()` method.

```python
# initialize result handler
result_handler = k2connect.ResultHandler

# process result 
processed_payload = result_handler.process(some_result)
```

#### Payload decomposer

Once a result is processed an a payload has been returned, it can be decomposed into its constituent result data using
the payload decomposer.
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
and [David Kariuki Mwangi](https://github.com/DavidJonKariz).

### Contributing

Bug reports and pull requests are welcome. Feel free raise issues on
our [issues tracker](https://github.com/kopokopo/k2-connect-python/issues)

### License

k2connect-python is [MIT](https://github.com/kopokopo/k2-connect-python/blob/master/LICENSE) Licensed.

### Changelog
