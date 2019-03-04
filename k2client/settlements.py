"""Handles transfer of funds to pre-approved settlement accounts (bank accounts or mobile wallets)."""
import requests
from k2client.json_builder import amount, transfer_object

# https://api-sandbox.kopokopo.com/transfers
default_transfers_url = ""


def settle(transfer_currency,
           transfer_value,
           transfer_destination=None):

    # define amount json object
    transfer_amount = amount(currency=transfer_currency, value=transfer_value)

    if transfer_destination is None:
        # define blind transfer json
        blind_transfer_object = transfer_object(amount=transfer_amount)

        # create blind transfer
        blind_transfer = requests.post(url=default_transfers_url, json=blind_transfer_object)

        return blind_transfer
    else:
        # define targeted transfer json
        targeted_transfer_object = transfer_object(amount=transfer_amount, destination=transfer_destination)

        # create targeted transfer
        targeted_transfer = requests.post(url=default_transfers_url, json=targeted_transfer_object)

        return targeted_transfer

