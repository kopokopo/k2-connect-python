"""
This module handles the initialization of the k2connect library.
It takes a client id, secret and base url and initializes all k2connect
services as with appropriate required arguments.
"""
# TODO: Remember to remove http from validation
# TODO: David-dev branch is the one that is behind use the development branch which is the updated one
from k2connect import exceptions

import k2connect

from .authorization import TokenService
from .k2_subscription__service import K2WebhookSubscriptionService
from .result_processor import ResultProcessor
from .receive_payments import ReceivePaymentsService
from . import validation
from .send_money_service import SendMoneyService
from .stk_push_service import StkPushService
from .transfer_account_service import TransferAccountService
from .notifications import NotificationService
from .polling_service import PollingService

Tokens = None
ReceivePayments = None
SendMoney = None
K2Stk = None
ExternalRecipient = None
TransferAccount = None
Webhooks = None
TransactionNotifications = None
ResultHandler = None
Polling = None
__version__ = '1.2.0'


def initialize(client_id, client_secret, base_url, api_secret=None):
    """
    Initializes k2connect services
    :param base_url: The domain to use in the library.
    :type base_url: str
    :param client_id: Identifier for the k2 user.
    :type client_id: str
    :param client_secret: Secret key for k2 user.
    :type client_secret: str
    :param api_secret: API Secret key for processing webhook payloads.
    :type api_secret: str
    """
    validation.validate_string_arguments(client_id,
                                         client_secret,
                                         base_url)
    validation.validate_base_url(base_url)

    # initialize  token service
    globals()['Tokens'] = TokenService(client_id=client_id,
                                       client_secret=client_secret,
                                       base_url=base_url)

    # initialize send money service
    globals()['SendMoney'] = lambda access_token=None: SendMoneyService(base_url=base_url, access_token=access_token)

    # initialize send money service
    globals()['K2Stk'] = lambda access_token=None: StkPushService(base_url=base_url, access_token=access_token)

    # initialize stk service
    globals()['ReceivePayments'] = ReceivePaymentsService(base_url=base_url)

    # initialize webhook service
    globals()['Webhooks'] = lambda access_token=None: K2WebhookSubscriptionService(base_url=base_url,
                                                                                   access_token=access_token)

    globals()['TransferAccount'] = lambda access_token=None: TransferAccountService(base_url=base_url,
                                                                                    access_token=access_token)

    # initialize transaction notification service
    globals()['TransactionNotifications'] = NotificationService(base_url=base_url)

    # initialize polling service
    globals()['Polling'] = lambda access_token=None: PollingService(base_url=base_url, access_token=access_token)

    # initialize response processor
    globals()['ResultHandler'] = ResultProcessor(base_url=base_url,
                                                 api_secret=api_secret)
