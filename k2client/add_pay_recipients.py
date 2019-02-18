"""Handles creating new pay recipients"""
import requests

# https://api-sandbox.kopokopo.com/pay_recipients
default_add_pay_recipient_url = ""


class AddPayRecipient(object):

    def __init__(self,
                 recipient_type,
                 pay_recipient,
                 first_name=None,
                 last_name=None,
                 email=None,
                 phone=None,
                 network=None,
                 name=None,
                 account_name=None,
                 bank_id=None,
                 bank_branch_id=None,
                 account_number=None):
        """

        :param recipient_type:
        :param pay_recipient:
        :param first_name:
        :param last_name:
        :param email:
        :param phone:
        :param network:
        :param name:
        :param account_name:
        :param bank_id:
        :param bank_branch_id:
        :param account_number:
        """
        self.recipient_type = recipient_type
        self.pay_recipient = pay_recipient
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.network = network
        self.name = name
        self.account_name = account_name
        self.bank_id = bank_id
        self.bank_branch_id = bank_branch_id
        self.account_number = account_number

    """Handles creation of pay recipient"""
    def create_pay_recipient(self):
        # define selected recipient type
        selected_recipient_type = self.recipient_type

        # check selected recipient type (Bank or Mobile Wallet)
        if selected_recipient_type is "bank_account":
            # define bank account pay recipient
            constructed_pay_recipient = bank_account_recipient_json_object_builder(self.name,
                                                                                   self.account_name,
                                                                                   self.bank_id,
                                                                                   self.bank_branch_id,
                                                                                   self.account_number,
                                                                                   self.email,
                                                                                   self.phone)
            # define pay recipient to be created
            created_recipient = recipient_json_object_builder(selected_recipient_type, constructed_pay_recipient)

            return created_recipient

        elif selected_recipient_type is "mobile_wallet":
            # define mobile wallet pay recipient
            constructed_pay_recipient = mobile_wallet_recipient_json_object_builder(self.first_name,
                                                                                    self.last_name,
                                                                                    self.phone,
                                                                                    self.network,
                                                                                    self.email)
            # define pay recipient to be created
            created_recipient = recipient_json_object_builder(selected_recipient_type, constructed_pay_recipient)

            # perform POST request to create pay recipient
            pay_recipient_creation_post_request = requests. post(default_add_pay_recipient_url, payload=created_recipient)

            return pay_recipient_creation_post_request


# build bank account pay recipient json object
def bank_account_recipient_json_object_builder(provided_name,
                                               provided_account_name,
                                               provided_bank_id,
                                               provided_bank_branch_id,
                                               provided_account_number,
                                               provided_email=None,
                                               provided_phone=None):
    bank_account_recipient_json_object = {
        "name": provided_name,
        "account_name": provided_account_name,
        "bank_id": provided_bank_id,
        "bank_branch_id": provided_bank_branch_id,
        "account_number": provided_account_number,
        "email": provided_email,
        "phone": provided_phone
    }
    return bank_account_recipient_json_object


# build mobile wallet pay recipient json object
def mobile_wallet_recipient_json_object_builder(provided_first_name,
                                                provided_last_name,
                                                provided_phone,
                                                provided_network,
                                                provided_email=None):
    mobile_wallet_recipient_json_object = {
        "first_name": provided_first_name,
        "last_name": provided_last_name,
        "phone": provided_phone,
        "network": provided_network,
        "email": provided_email
    }
    return mobile_wallet_recipient_json_object


# build recipient json object for pay recipient to be created
def recipient_json_object_builder(provided_recipient_type, provided_pay_recipient):

    recipient_json_object = {
        "type": provided_recipient_type,
        "pay_recipient": provided_pay_recipient
    }
    return recipient_json_object


# get created pay recipient data loaction
def location(response):
    pay_recipient_location = response.headers.get('location')
    return pay_recipient_location