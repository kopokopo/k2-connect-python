"""Handles building json objects across the library """
import requests

"""Build JSON objects responsible for creating PAY recipients"""


# build bank account pay recipient json object
def bank_account_recipient(provided_name,
                           provided_account_name,
                           provided_bank_id,
                           provided_bank_branch_id,
                           provided_account_number,
                           provided_email=None,
                           provided_phone=None):
    bank_account_recipient_object = {
        "name": provided_name,
        "account_name": provided_account_name,
        "bank_id": provided_bank_id,
        "bank_branch_id": provided_bank_branch_id,
        "account_number": provided_account_number,
        "email": provided_email,
        "phone": provided_phone
    }
    return bank_account_recipient_object


# build mobile wallet pay recipient json object
def mobile_wallet_recipient(provided_first_name,
                            provided_last_name,
                            provided_phone,
                            provided_network,
                            provided_email=None):
    mobile_wallet_recipient_object = {
        "first_name": provided_first_name,
        "last_name": provided_last_name,
        "phone": provided_phone,
        "network": provided_network,
        "email": provided_email
    }
    return mobile_wallet_recipient_object


# build recipient json object for pay recipient to be created
def pay_recipient(provided_recipient_type, provided_pay_recipient):
    recipient_object = {
        "type": provided_recipient_type,
        "pay_recipient": provided_pay_recipient
    }
    return recipient_object


"""Build JSON Objects responsible for creating MPESA payment requests"""


# build subscriber json object
def subscriber(provided_first_name,
               provided_last_name,
               provided_phone,
               provided_email):
    subscriber_object = {
        "first_name": provided_first_name,
        "last_name": provided_last_name,
        "phone": provided_phone,
        "email": provided_email
    }
    return subscriber_object


# build amount json object
def amount(provided_currency, provided_value):
    amount_object = {
        "currency": provided_currency,
        "value": provided_value
    }
    return amount_object


# build metadata json object
def metadata(**kwargs):
    metadata_object = kwargs
    return metadata_object


# build links json object
def links(provided_call_back_url):
    links_object = {
        "call_back_url": provided_call_back_url
    }
    return links_object


# build payment request json object
def payment_request(provided_payment_channel,
                    provided_till_identifier,
                    provided_subscriber,
                    provided_amount,
                    provided_links,
                    provided_metadata=None):
    payment_object = {
        "payment_channel": provided_payment_channel,
        "till_identifier": provided_till_identifier,
        "subscriber": provided_subscriber,
        "amount": provided_amount,
        "metadata": provided_metadata,
        "links": provided_links
    }
    return payment_object


"""Build JSON Objects for cretaing webhook subscriptions"""


# webhook json object builder
def webhook_subscription(provided_event_type,
                         provided_url,
                         provided_webhook_secret):
    webhook_subscription_object = {
        "event_type": provided_event_type,
        "url": provided_url,
        "webhook_secret": provided_webhook_secret
    }
    return webhook_subscription_object
