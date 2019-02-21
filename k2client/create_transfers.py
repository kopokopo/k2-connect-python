"""Handles transfer of funds to pre-approved settlement accounts (bank accounts or mobile wallets)."""
import requests

# https://api-sandbox.kopokopo.com/transfers
default_transfers_url = ""


class CreateTransfers(object):
    def __init__(self,
                 transfer_currency=None,
                 transfer_value=None,
                 transfer_destination=None):

        """
        :param transfer_currency:
        :param transfer_value:
        :param transfer_destination:
        """
        self.transfer_currency = transfer_currency
        self.transfer_value = transfer_value
        self.transfer_destination = transfer_destination

    def create_transfer(self):
        # define amount json object
        amount = transfer_amount_json_object_builder(provided_currency=self.transfer_currency,
                                                     provided_value=self.transfer_value)
        # perform create transfer post request
        if self.transfer_destination is not None:
            transfer_json_object = {
                "amount": amount,
                "destination": self.transfer_destination
            }
            create_targeted_transfer_post_request = requests.post(url=default_transfers_url, json=transfer_json_object)
            return create_targeted_transfer_post_request
        else:
            transfer_json_object = {
                "amount": amount
            }
            create_blind_transfer_post_request = requests.post(url=default_transfers_url, json=transfer_json_object)
            return create_blind_transfer_post_request


# transfer amount json object builder
def transfer_amount_json_object_builder(provided_currency, provided_value):
    transfer_amount_json_object = {
        "currency": provided_currency,
        "value": provided_value
    }
    return transfer_amount_json_object
