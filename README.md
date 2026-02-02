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
- [PaymentLinks](#payment-links-service)
- [ReversalService](#reversal-service)
- [IncomingPaymentsService](#incoming-payments-service)
- [TransferAccountService](#transfers-account-service)
- [WebhookService](#webhook-subscription-service)
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
    "callback_url": "https://callback_to_your_app.your_application.com",
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

#### Incoming payments service

The incoming payments service allows you to create requests for incoming payments over a specific channel and receive
the
payments to your account. You can also check the status of your payment requests and access the payment request through
a URL.

In order to create a payment request, the `create_incoming_payment()` method is used. This method can be passed the
following arguments:

* first_name `REQUIRED`
* last_name `REQUIRED`
* callback_url `REQUIRED`
* payment_channel `REQUIRED`
* phone `REQUIRED`
* till_number `REQUIRED`
* value `REQUIRED`
* currency='KES' `REQUIRED`
* metadata `OPTIONAL`. Maximum 5 dictionaries/hashes/key-value pairs.

The status of a payment request can be checked through the `view_incoming_payment()` method and passing the reference of
the payment.

```python
import k2connect

incoming_payments_service = k2connect.IncomingPaymentsService(access_token=access_token)

# create an incoming request
request_payload = {
    "payment_channel": "MPESA",
    "till_number": "K112233",
    "subscriber": {
        "first_name": "python_first_name",
        "last_name": "python_last_name",
        "email": "daivd.j.kariuki@gmail.com",
        "phone_number": "+254911222536",
    },
    "amount": {
        "currency": "KES",
        "value": 10
    },
    "callback_url": "https://callback_to_your_app.your_application.com",
    "metadata": {"key": "value"}
}
mpesa_payment_location = incoming_payments_service.create_incoming_payment(request_payload)
```

#### Transfers account service

The Transfer Accounts service allows you to create verified transfer accounts for both bank accounts and mobile wallets.
These accounts can then be used as recipients for payouts and transfers. Depending on the account type, different
parameters are required.

**Bank Transfer Account**

Use this option to create a verified merchant bank account.

Required parameters:

* `type` – Must be set to **merchant_bank_account**
* `account_name` – Name of the bank account holder
* `account_number` – Bank account number
* `bank_branch_ref` – Reference for the bank branch
* `settlement_method` – Settlement method; one of RTS or EFT

Optional parameters:
* `nickname` - A friendly name of the account


**M-Pesa Transfer Account**

Required parameters:

* `type` - must be set to **merchant_wallet**
* `first_name` - Recipient's first name
* `last_name` - Recipient's last name
* `phone_number` - Recipient's phone number
* `network` - Mobile network; currently supported: **Safaricom**

Optional parameters:
* `email` – Recipient’s email address 
* `nickname` – A friendly name for the account

```python
import k2connect

transfer_service = k2connect.TransferAccount(access_token=access_token)

# create verified bank transfer account
request_payload = {
    "settlement_method": 'RTS',
    "account_name": 'py_sdk_account_name',
    "account_number": 'py_sdk_account_number',
    "bank_branch_ref": '633aa26c-7b7c-4091-ae28-96c0687cf886'
}
bank_transfer_account_location = transfer_service.add_transfer_account(request_payload)
# https://sandbox.kopokopo.com/api/v2/merchant_bank_accounts/b794421d-6038-45dc-b088-8c8764977aba

# create verified mpesa transfer account
request_payload = {
    "first_name": 'py_sdk_first_name',
    "last_name": 'py_sdk_last_name',
    "phone_number": '+254911222538',
    "network": 'Safaricom'
}
mpesa_transfer_account_location = transfer_service.add_transfer_account(request_payload)
# https://sandbox.kopokopo.com/api/v2/merchant_wallets/3a1163c7-dfb9-4f05-bf35-73b69db89bae
```

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
import k2connect

# initialize service
webhook_service = k2connect.Webhooks(access_token=access_token)

request_payload = {
    "event_type": 'buygoods_transaction_received',
    "webhook_uri": 'https://webhook.site/52fd1913-778e-4ee1-bdc4-74517abb758d',
    "scope": 'till',
    "scope_reference": '112233',
    "enable_daraja_payload": True
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
    "callback_url": "https://callback_to_your_app.your_application.com",
    "webhook_event_reference": "d81312b9-4c0e-4347-971f-c3d5b14bdbe4",
    "message": 'Alleluia',
}
notification_resource_location_url = notification_service.send_transaction_sms_notification(request_payload)

# get request status
request_status = notification_service.transaction_notification_status(access_token, notification_resource_location_url)
```

For more information, please
read [Transaction Notification Docs](https://api-docs.kopokopo.com/#transaction-sms-notifications)

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
import k2connect

# initialize service
polling_service = k2connect.Polling(access_token=access_token)

# initiating a polling request
request_payload = {
    "scope": "till",
    "scope_reference": "112233",
    "from_time": "2021-07-09T08:50:22+03:00",
    "to_time": "2021-07-10T18:00:22+03:00",
    "callback_url": "https://callback_to_your_app.your_application.com",
}
polling_resource_location_url = polling_service.initiate_polling_request(request_payload)

# get request status
request_status = polling_service.polling_request_status(polling_resource_location_url)
```

#### Payment links service

Payment links allow you to create and share payment requests with customers. This service allows you to create, view and
cancel payment links

* amount: The amount of payment being requested `REQUIRED`
* currency: The currency for the amount. Currently, only `KES` is supported `REQUIRED`
* tillNumber: The till number to which the payment is to be made `REQUIRED`
* callbackUrl: Url that the result will be posted to `REQUIRED`
* paymentReference: This is a unique reference that you can use to track the payment link `OPTIONAL`
* note: An additional note to be seen by the customer when they click the payment link. You can include the payment
  reason `OPTIONAL`
* paymentLinkReference: This is the unique reference generated for a created payment link. It is required to view the
  status or cancel the payment link

```python
import k2connect

# initialize service
payment_links_service = k2connect.PaymentLinks(access_token=access_token)

# create a payment link
request_payload = {
    "currency": "KES",
    "amount": 20000,
    "till_number": "65328",
    "payment_reference": "UNIQUE_REFERENCE",
    "note": "Payment for TV sold",
    "callback_url": "https://callback_to_your_app.your_application.com",
}
payment_link_resource_location_url = payment_links_service.create_payment_link(request_payload)

# view payment link
request_body = {
    "payment-link-reference": "payment-link-reference"
}
payment_link_resource = payment_links_service.get_status(request_body)

# cancel payment link
request_body = {
    "payment-link-reference": "payment-link-reference"
}
payment_links_service.cancel_payment_link(request_body)
```

#### Reversal service

This service allows you to initiate a reversal for a transaction and view its status

* transactionReference: The external reference of the transaction to be reversed `REQUIRED`
* reason: The reason for reversing the transaction `REQUIRED`
* callbackUrl: Url that the result will be posted to `REQUIRED`
* reversalReference: This is the unique reference generated for an initiated reversal. It is required to view the status
  of the reversal

```python
import k2connect

# initialize service
reversal_service = k2connect.Reversals(access_token=access_token)

# initiating a reversal request
request_payload = {
    "transaction_reference": "CX83943KH",
    "reason": "Wrong payment",
    "callback_url": "https://webhook.site/52fd1913-778e-4ee1-bdc4-74517abb758d",
}
reversal_resource_location_url = reversal_service.initiate_reversal(request_payload)
# https://sandbox.kopokopo.com/api/v2/reversals/247b1bd8-f5a0-4b71-a898-f62f67b8ae1c

# get reversal status
request_body = {
    "reversal-reference": "247b1bd8-f5a0-4b71-a898-f62f67b8ae1c"
}
reversal_resource = reversal_service.get_status(request_body)
```

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
