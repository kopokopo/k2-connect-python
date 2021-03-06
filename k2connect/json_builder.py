"""
This module handles the building of JSON objects for HTTPS requests
in the k2-connect library. It serializes python dictionaries to a JSON
formatted strings.
Example:
    >>>import json
    >>>sample_dict = {'key': 'value'}
    >>>print(json.dumps(sample_dict))
    "{"key": "value"}"
"""
import json
from k2connect import exceptions
from k2connect import validation


# serialize python dicts to JSON str
def serializer(dictionary):
    """
    Serializes python dict to json formatted str.
    Returns str.

    :param dictionary:
    :type dictionary: dict
    :return: str
    """
    validation.validate_dictionary_arguments(dictionary)
    return json.dumps(dictionary)


# special function
def metadata(join=None, **kwargs):
    """
    Returns a json formatted str with a maximum of 5 metadata key-value pairs.
    :param join:
    :param kwargs: Metadata information
    :return: str
    """
    if kwargs is None or kwargs == '':
        raise exceptions.InvalidArgumentError('Invalid argument passed. Expects ' / 'key=word/')
    if len(kwargs) >= 5:
        raise exceptions.InvalidArgumentError('Should be less than or 5 metadata objects')
    metadata_object = kwargs
    return serializer(metadata_object)


def links(callback_url):
    """
    Validates url passed. Returns a str containing a callback_url.
    :param callback_url: Callback URL to post result.
    :type callback_url: str
    :return: str
    """
    # validate string argument
    validation.validate_string_arguments(callback_url)

    # validate url value
    validation.validate_url(callback_url)

    links_object = {'callback_url': callback_url}
    return serializer(links_object)


def amount(currency, value):
    """
    Returns json formatted str containing currency and value.
    :param currency: Currency of amount
    :type currency: str
    :param value: Value of money
    :type value: str
    :return: str
    """
    # validate str arguments
    validation.validate_string_arguments(currency, value)

    amount_object = {'currency': currency,
                     'value': value
                     }
    return serializer(amount_object)


def bank_account(account_name,
                 account_number,
                 bank_branch_id,
                 bank_id,
                 name,
                 **kwargs):
    """
    Returns a json formatted str with the optional value of email and phone.
    Checks if optional values are present, else passes values as null.
    :param account_name: Name as indicated on the bank account name.
    :type account_name: str
    :param account_number: Bank account number.
    :type account_number: str
    :param bank_branch_id: Identifier identifying the destination bank branch.
    :type bank_branch_id: str
    :param bank_id: Identifier identifying the destination bank
    :type bank_id: str
    :param name: Name of the receiving entity.
    :type name: str
    :param kwargs: Provision for optional 'email' and 'phone' information.
    :type kwargs: kwargs
    :return: str
    """
    # validate string arguments
    validation.validate_string_arguments(account_name,
                                         account_number,
                                         bank_branch_id,
                                         bank_id,
                                         name)
    if 'email' not in kwargs:
        email = 'Null'
    else:
        email = kwargs['email']
    if 'phone' not in kwargs:
        phone = 'Null'
    else:
        phone = kwargs['phone']

    bank_account_object = {'account_name': account_name,
                           'account_number': account_number,
                           'bank_branch_id': bank_branch_id,
                           'bank_id': bank_id,
                           'name': name,
                           'email': email,
                           'phone': phone}
    return serializer(bank_account_object)


def bank_settlement_account(account_name,
                            account_number,
                            bank_ref,
                            bank_branch_ref):
    """
    Returns a json formatted str with bank settlement account information.
    :param account_name: The name as indicated on the bank account name
    :type account_name: str
    :param account_number: The bank account number
    :type account_number: str
    :param bank_ref: An identifier identifying the destination bank
    :type bank_ref: str
    :param bank_branch_ref: An identifier identifying the destination bank branch
    :type bank_branch_ref: str
    """
    # validate string arguments
    validation.validate_string_arguments(account_name,
                                         account_number,
                                         bank_ref,
                                         bank_branch_ref)

    bank_settlement_account_object = {'account_name': account_name,
                                      'account_number': account_number,
                                      'bank_ref': bank_ref,
                                      'bank_branch_ref': bank_branch_ref
                                      }
    return serializer(bank_settlement_account_object)


def mobile_wallet(first_name,
                  last_name,
                  phone,
                  network,
                  **kwargs):
    """
    Returns a json formatted str with the optional value of email.
    Checks if optional value is present, else passes values as null.

    :param first_name: First name of the recipient.
    :type first_name: str
    :param last_name: Last name of the recipient.
    :type last_name: str
    :param phone: Phone number of recipient.
    :type phone: str
    :param network: The mobile network to which the phone number belongs.
    :type network: str
    :param kwargs: Provision for optional 'email' value
    :type kwargs: kwargs
    :return:
    """
    # validate string arguments
    validation.validate_string_arguments(first_name,
                                         last_name,
                                         phone,
                                         network)

    if 'email' not in kwargs:
        email = 'Null'
    else:
        email = kwargs['email']

    mobile_wallet_object = {'first_name': first_name,
                            'last_name': last_name,
                            'phone': phone,
                            'network': network,
                            'email': email
                            }
    return serializer(mobile_wallet_object)


def pay_recipient(recipient_type, recipient):
    """
    Returns json formatted str containing pay recipient object.
    :param recipient_type: Type of recipient eg. mobile wallet
    or bank account
    :type recipient_type: str
    :param recipient: JSON formatted str containing details of the
    recipient
    :type recipient: str
    :return: str
    """
    # validate string arguments
    validation.validate_string_arguments(recipient, recipient_type)

    recipient_object = {'type': recipient_type, 'pay_recipient': recipient}
    return serializer(recipient_object)


def subscriber(first_name,
               last_name,
               phone,
               **kwargs):
    """
    Returns JSON formatted str containing subscriber information
    :param first_name: First name of the subscriber
    :type first_name: str
    :param last_name: Last name of the subscriber
    :type last_name: str
    :param phone: Phone number of the subscriber from which the
    pay will be made
    :type phone: str
    :param kwargs: Provision for optional 'email' information.
    :type kwargs: str
    :return: str
    """
    # validate string arguments
    validation.validate_string_arguments(first_name,
                                         last_name,
                                         phone)
    if 'email' not in kwargs:
        email = 'Null'
    else:
        email = kwargs['email']

    subscriber_object = {'first_name': first_name,
                         'last_name': last_name,
                         'phone': phone,
                         'email': email}

    return serializer(subscriber_object)


def mpesa_payment(mpesa_links,
                  mpesa_payment_amount,
                  mpesa_payment_subscriber,
                  payment_channel,
                  till_number,
                  **kwargs):
    """
    Returns JSON formatted str with optional 'metadata' JSON str object.
    :param mpesa_links: A JSON object containing the call back URL
    :type mpesa_links: str
    :param payment_channel: Payment channel e.g MPESA
    :type payment_channel: str
    :param till_number: Till to which the pay is made.
    :type till_number: str
    :param mpesa_payment_subscriber: Subscriber JSON object.
    :type mpesa_payment_subscriber str
    :param mpesa_payment_amount: Amount JSON object.
    :type mpesa_payment_amount str
    :param kwargs: Optional JSON object containing a maximum of 5 key
    value pairs.
    :return: str
    """

    # validate string arguments
    validation.validate_string_arguments(mpesa_links,
                                         mpesa_payment_amount,
                                         mpesa_payment_subscriber,
                                         payment_channel,
                                         till_number)

    if 'metadata' not in kwargs:
        mpesa_payment_metadata = 'Null'
    else:
        mpesa_payment_metadata = kwargs['metadata']

    mpesa_payment_object = {'payment_channel': payment_channel,
                            'till_identifier': till_number,
                            'subscriber': mpesa_payment_subscriber,
                            'amount': mpesa_payment_amount,
                            'metadata': mpesa_payment_metadata,
                            '_links': mpesa_links
                            }

    return serializer(mpesa_payment_object)


def webhook_subscription(event_type,
                         webhook_endpoint,
                         webhook_secret):
    """
    Returns JSON formatted str containing webhook subscription information
    :param event_type:The type of event subscribed to.
    :type event_type:  str
    :param webhook_endpoint: The HTTP end point to send the webhook.
    :type webhook_endpoint: str
    :param webhook_secret: A string that will be used to encrypt the request
    payload using HMAC.
    :type webhook_secret: str
    :return: str
    """

    # validate string arguments
    validation.validate_string_arguments(event_type,
                                         webhook_endpoint,
                                         webhook_secret)

    webhook_subscription_object = {'event_type': event_type,
                                   'url': webhook_endpoint,
                                   'webhook_secret': webhook_secret
                                   }
    return serializer(webhook_subscription_object)


def pay(payment_destination,
        payment_amount,
        payment_metadata,
        payment_links):
    """
    Return JSON formatted str containing information about a transfer.
    :param payment_destination: ID of the destination of funds.
    :type payment_destination : str
    :param payment_amount: A JSON formatted str containing the currency
    and the amount to be transferred.
    :type payment_amount: str
    :param payment_metadata: A JSON formatted str with a maximum of 5
    key-value pairs.
    :type payment_metadata: str
    :param payment_links:A JSON formatted str containing a call back URL.
    :type payment_links: str
    :return: str
    """

    # validate string arguments
    validation.validate_string_arguments(payment_destination,
                                         payment_amount,
                                         payment_metadata,
                                         payment_links)

    payment_json_object = {
        "destination": payment_destination,
        "amount": payment_amount,
        "metadata": payment_metadata,
        "_links": payment_links
    }
    return serializer(payment_json_object)


def transfers(transfers_amount,
              **kwargs):
    """
    Returns JSON formatted containing information about a transfer.
    :param transfers_amount: Amount to be transferred.
    :type transfers_amount: str
    :param kwargs: Provision for optional 'destination' value.
    :type kwargs: str
    :return: str
    """

    # validate string arguments
    validation.validate_string_arguments(transfers_amount)

    if 'transfer_destination' not in kwargs:
        destination = 'Null'
    else:
        destination = kwargs['transfer_destination']

    transfers_object = {'amount': transfers_amount,
                        'destination': destination
                        }
    return serializer(transfers_object)
