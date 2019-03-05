import k2client


from k2client import pay
from k2client import recieve_mpesa
from k2client import transfers
from k2client import webhooks
from k2client import exceptions


def initalize(client_id, client_secret):
    if client_id or client_secret is None:
        raise exceptions.ValueEmptyError('Values cannot be empty ')
    if type(client_id) or type(client_secret) is not str:
        raise exceptions.InvalidEventTypeError
