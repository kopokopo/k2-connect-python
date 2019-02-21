"""Handles creating new pay recipients"""
import requests
from .json_builder import bank_account_recipient, mobile_wallet_recipient, pay_recipient

# https://api-sandbox.kopokopo.com/pay_recipients
default_add_pay_recipient_url = ""


class AddPayRecipient(object):

    def __init__(self,
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
        if selected_recipient_type is "bank_account_recipient":
            # define bank account pay recipient
            constructed_pay_recipient = bank_account_recipient(
                provided_name=self.name,
                provided_account_name=self.account_name,
                provided_bank_id=self.bank_id,
                provided_bank_branch_id=self.bank_branch_id,
                provided_account_number=self.account_number,
                provided_email=self.email,
                provided_phone=self.phone)
            # define pay recipient to be created
            created_recipient = pay_recipient(provided_recipient_type=selected_recipient_type,
                                              provided_pay_recipient=constructed_pay_recipient)

            # perform POST request to create pay recipient
            create_pay_request = requests.post(url=default_add_pay_recipient_url,
                                               payload=created_recipient)

            return create_pay_request

        elif selected_recipient_type is "mobile_wallet":
            # define mobile wallet pay recipient
            constructed_pay_recipient = mobile_wallet_recipient(provided_first_name=self.first_name,
                                                                provided_last_name=self.last_name,
                                                                provided_phone=self.phone,
                                                                provided_network=self.network,
                                                                provided_email=self.email)
            # define pay recipient to be created
            created_recipient = pay_recipient(provided_recipient_type=selected_recipient_type,
                                              provided_pay_recipient=constructed_pay_recipient)

            # perform POST request to create pay recipient
            create_pay_request = requests.post(url=default_add_pay_recipient_url,
                                               payload=created_recipient)

            return create_pay_request


# get created pay recipient data loaction
def location(response):
    pay_recipient_location = response.headers.get('location')
    return pay_recipient_location
