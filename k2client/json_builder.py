"""Handles building json objects across the library """


# build metadata json object
def metadata(metadata_dictionary):
    """
    :param metadata_dictionary: A JSON containing upto a maximum of 5 key-value pairs for the developer's own use
    :return: dictionary
    """
    metadata_object = metadata_dictionary
    return metadata_object


# build links json object
def links(links_self=None,
          links_call_back_url=None):
    """
    :param links_self: Link pointing to a specific result for a request made by k2-connect
    :type links_self: str
    :param links_call_back_url: Callback URL where the result of a request to KopoKopo will be posted
    :type links_call_back_url: str
    :return:A JSON containing links where the results will be posted. MUST be a secure HTTPS (TLS) endpoint
    """
    links_object = {
        "self": links_self,
        "call_back_url": links_call_back_url,
        "payment_request": links_payment_request
    }
    return links_object


# build amount json object
def amount(currency, value):
    """
    :param value: Value of money to be sent (child of amount JSON)
    :type value: str
    :param currency: Currency of amount being transacted
    :type currency: str
    :return: A JSON object containing the currency and the amount to be transferred
    """
    amount_object = {
        "currency": currency,
        "value": value
    }
    return amount_object


# build bank account pay recipient json object
def bank_account(**kwargs):
    """
    :param kwargs: Key worded arguments to build bank_account JSON object
    :return: A JSON object containing information about a bank account
    """
    bank_account_object = kwargs
    return bank_account_object


"""Build JSON objects responsible for creating PAY recipients"""


# build mobile wallet pay recipient json object
def mobile_wallet(first_name,
                  last_name,
                  phone,
                  network,
                  email=None):
    """
    :param first_name: First name of the recipient
    :type first_name: str
    :param last_name: Last name of the recipient
    :type last_name: str
    :param email: Email address of recipient
    :type email: str
    :param phone: Phone number of recipient
    :type phone: str
    :param network: The mobile network to which the phone number belongs
    :type network: str
    :return: A JSON object containing information about a mobile wallet
    """
    mobile_wallet_object = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "network": network,
        "email": email
    }
    return mobile_wallet_object


# build recipient json object for pay recipient to be created
def pay_recipient(recipient_type, recipient):
    """
    :param recipient_type: The type of the recipient eg. mobile wallet or bank account
    :type recipient_type: str
    :param recipient: A JSON object containing details of the recipient
    :type recipient: json
    :return: A JSON object containing information about a pay recipient
    """
    recipient_object = {
        "type": recipient_type,
        "pay_recipient": recipient
    }
    return recipient_object


"""Build JSON Objects responsible for creating MPESA payment requests"""


# build subscriber json object
def subscriber(first_name,
               last_name,
               phone,
               email=None):
    """
    :param first_name: First name of the subscriber
    :type first_name: str
    :param last_name: Last name of the subscriber
    :type last_name: str
    :param email: Email address of subscriber
    :type email: str
    :param phone: Phone number of subscriber
    :type phone: str
    :return: A JSON object containing information about a subscriber
    """
    subscriber_object = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email
    }
    return subscriber_object


# build payment request json object
def stk_request(payment_channel,
                till_number,
                stk_subscriber,
                stk_amount,
                stk_links,
                stk_metadata=None):
    """
    :param payment_channel: The payment channel to be used eg. MPESA
    :type payment_channel: str
    :param till_number:The till to which the payment will be made
    :type till_number: str
    :param stk_subscriber: A Subscriber JSON object see below
    :type stk_subscriber: json
    :param stk_amount:	An Amount JSON object containing currency and amount
    :type stk_amount: json
    :param stk_links:A JSON object containing the call back URL where the result of the Payment Request will be posted
    :type stk_links: json
    :param stk_metadata:An optional JSON object containing a maximum of 5 key value pairs
    :type stk_metadata: json
    :return:
    """
    payment_object = {
        "payment_channel": payment_channel,
        "till_identifier": till_number,
        "subscriber": stk_subscriber,
        "amount": stk_amount,
        "metadata": stk_metadata,
        "links": stk_links
    }
    return payment_object


"""Build JSON Objects for creating webhook subscriptions"""


# webhook json object builder
def webhook_subscription(event_type,
                         webhook_endpoint,
                         webhook_secret):
    """
    :param event_type:The type of event you are subscribing to. Should be one of; buygoods_transaction_received, buygoods_transaction_reversed, settlement_transfer_completed, customer_created
    :type event_type:  str
    :param webhook_endpoint: The http end point to send the webhook. MUST be secured with HTTPS (TLS)
    :type webhook_endpoint: str
    :param webhook_secret: A string that will be used to encrypt the request payload using HMAC
    :type webhook_secret: str
    :return: A JSON object containing information about a webhook subscription
    """
    webhook_subscription_object = {
        "event_type": event_type,
        "url": webhook_endpoint,
        "webhook_secret": webhook_secret
    }
    return webhook_subscription_object


""""Build JSON Objects for creating payments"""


# build payment json object
def payment(provided_destination,
            provided_amount,
            provided_metadata,
            provided_links):
    """
    :param provided_destination: ID of the destination (pay recipient) of funds (bank account or mobile wallet
    :type provided_destination : str
    :param provided_amount: A JSON object containing the currency and the amount to be transferred
    :type provided_amount: json
    :param provided_metadata: A JSON containing upto a maximum of 5 key-value pairs for your own use
    :type provided_metadata:json
    :param provided_links:A JSON containing a call back URL where the results of the Payment will be posted. MUST be a secure HTTPS (TLS) endpoint
    :type provided_links: json
    :return: A JSON object containing information about a transfer
    """
    payment_json_object = {
        "destination": provided_destination,
        "amount": provided_amount,
        "metadata": provided_metadata,
        "_links": provided_links
    }
    return payment_json_object


""""Build JSON Objects for creating payments"""


def transfers(**kwargs):
    """
    :param kwargs: Key worded arguments to build transfers JSON object
    :return: A JSON object containing information about a transfer
    """
    transfer_json_object = kwargs
    return transfer_json_object