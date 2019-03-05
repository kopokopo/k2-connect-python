"""Handles building json objects across the library """


# build metadata json object
def metadata(metadata_dictionary):
    metadata_object = metadata_dictionary
    return metadata_object


# build links json object
def links(links_self=None,
          links_call_back_url=None,
          links_payment_request=None, ):
    links_object = {
        "self": links_self,
        "call_back_url": links_call_back_url,
        "payment_request": links_payment_request
    }
    return links_object


# build amount json object
def amount(currency, value):
    amount_object = {
        "currency": currency,
        "value": value
    }
    return amount_object


# build bank account pay recipient json object
def bank_account(**kwargs):
    bank_account_object = kwargs
    return bank_account_object


"""Build JSON objects responsible for creating PAY recipients"""


# build mobile wallet pay recipient json object
def mobile_wallet(first_name,
                  last_name,
                  phone,
                  network,
                  email=None):
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
    subscriber_object = {
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone,
        "email": email
    }
    return subscriber_object


# build payment request json object
def stk_request(payment_channel,
                till_identifier,
                stk_subscriber,
                stk_amount,
                stk_links,
                stk_metadata=None):
    payment_object = {
        "payment_channel": payment_channel,
        "till_identifier": till_identifier,
        "subscriber": stk_subscriber,
        "amount": stk_amount,
        "metadata": stk_metadata,
        "links": stk_links
    }
    return payment_object


"""Build JSON Objects for creating webhook subscriptions"""


# webhook json object builder
def webhook_subscription(event_type,
                         url,
                         webhook_secret):
    webhook_subscription_object = {
        "event_type": event_type,
        "url": url,
        "webhook_secret": webhook_secret
    }
    return webhook_subscription_object


""""Build JSON Objects for creating payments"""


# build payment json object
def payment(provided_destination,
            provided_amount,
            provided_metadata,
            provided_links):
    payment_json_object = {
        "destination": provided_destination,
        "amount": provided_amount,
        "metadata": provided_metadata,
        "_links": provided_links
    }
    return payment_json_object


""""Build JSON Objects for creating payments"""


def transfers(**kwargs):
    transfer_json_object = kwargs
    return transfer_json_object