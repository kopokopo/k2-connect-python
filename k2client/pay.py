"""Handles creating an outgoing payment to a third party."""
import requests
from .service import Service
from .json_builder import amount, metadata, links, pay_recipient

# for sandbox:
# https://api-sandbox.kopokopo.com/payments
# https://api-sandbox.kopokopo.com/pay_recipients
# for production:
# https://api.kopokopo.com/payments
# https://api.kopokopo.com/pay_recipients
add_pay_path = "pay_recipients"
send_pay_path = "payments"


class PayService(Service):
    def __init__(self,
                 bearer_token,
                 recipient_type):
        """
        :param bearer_token:
        :param recipient_type:
        """
        super(PayService, self).__init__(client_id=self._client_id, client_secret=self._client_id)
        self._bearer_token = bearer_token
        self.recipient_type = recipient_type

    def add_pay_recipient(self,
                          email=None,
                          phone=None,
                          first_name=None,
                          last_name=None,
                          network=None,
                          name=None,
                          account_name=None,
                          bank_id=None,
                          bank_branch_id=None,
                          account_number=None
                          ):
        """
        :param email: Email address of recipient
        :type email: str
        :param phone: Phone number of recipient
        :type phone: str
        :param first_name: First name of the recipient
        :type first_name: str
        :param last_name: Last name of the recipient
        :type last_name: str
        :param network: The mobile network to which the phone number belongs
        :type network: str
        :param name: Name of the receiving entity
        :type name: str
        :param account_name: The name as indicated on the bank account name
        :type account_name:str
        :param bank_id:  An identifier identifying the destination bank
        :type bank_id: str
        :param bank_branch_id: An identifier identifying the destination bank branch
        :type bank_branch_id: str
        :param account_number: The bank account number
        :type account_number: str
        :return: http response object
        """
        # build url
        url = self.build_url(add_pay_path)

        # validate email and phone number
        if validation.validate_phone_number(self.phone) is True:
            pass
        elif self.email is not None:
            if validation.validate_email(self.email) is True:
                pass
        else:
            if self.recipient_type == 'bank_account':
                # define bank account pay recipient
                recipient_object = bank_account(name=name,
                                                account_name=account_name,
                                                bank_id=bank_id,
                                                bank_branch_id=bank_branch_id,
                                                account_number=account_number,
                                                email=email,
                                                phone=phone)

                # define pay recipient to be created
                recipient = pay_recipient(recipient_type=self.recipient_type,
                                          recipient=recipient_object)

                return self.make_requests(url=url, method='POST', payload=recipient, headers=self._headers)

            elif self.recipient_type == 'mobile_wallet':
                # define mobile wallet pay recipient
                recipient_object = mobile_wallet(first_name=first_name,
                                                 last_name=last_name,
                                                 phone=phone,
                                                 network=network,
                                                 email=email)
                # define pay recipient to be created
                recipient = pay_recipient(recipient_type=self.recipient_type,
                                          recipient=recipient_object)

                return self.make_requests(url=url, method='POST', payload=recipient, headers=self._headers)

    def send_pay(self,
                 destination,
                 value,
                 callback_url,
                 currency='KES'):
        """
        :param destination: ID of the destination (pay recipient) of funds (bank account or mobile wallet
        :type  destination: str
        :param value: Value of money to be sent (child of amount JSON)
        :type value: str
        :param callback_url: Callback URL where the results of the Payment will be posted. MUST be a secure HTTPS (TLS) endpoint
        :type callback_url: str
        :param currency: Currency of amount being transacted
        :type currency: str
        :return: http response object
        """

        # build url
        url = self.build_url(url_path=pay_path)

        # define amount json object
        payment_amount = amount(currency=currency, value=value)

        # define metadata json object
        metadata_object = {k: v for (k, v) in self.kwargs.items()}
        payment_metadata = metadata(metadata_object)

        # define links json object
        payment_links = links(links_call_back_url=callback_url)

        # define payment json object
        payment_object = payment(destination=destination,
                                 amount=payment_amount,
                                 metadata=payment_metadata,
                                 links=payment_links)

        return self.make_requests(url=url, headers=self._headers, payload=payment_object, method='POST')

    def pay_status(self, response):
        """
        :param response: Http response object containing resource location
        :return: http response object
        """
        # define query location
        query_location = ResourceLocation(response).get_location()

        # define query status object
        query_status_object = QueryStatus(bearer_token=self._bearer_token)

        return query_status_object.query_transaction_status(query_location)
