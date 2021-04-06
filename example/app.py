import json

from flask import Flask, render_template, request
import k2connect
import datetime
from os import environ
from k2connect import payload_decomposer

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/token', methods=['GET'])
def access_token():
    return render_template('token.html')


@app.route('/request_token', methods=['POST'])
def request_token():
    environ['CLIENT_ID'] = request.form['client-id']
    environ['CLIENT_SECRET'] = request.form['client-secret']
    given_time = datetime.datetime.now()

    k2connect.initialize(environ['CLIENT_ID'], environ['CLIENT_SECRET'], 'http://127.0.0.1:3000/')
    token_service = k2connect.Tokens
    access_token_request = token_service.request_access_token()
    environ['ACCESS_TOKEN'] = token_service.get_access_token(access_token_request)

    return render_template('token.html', client_id=environ.get('CLIENT_ID'), client_secret=environ.get('CLIENT_SECRET'),
                           given_time=given_time, access_token=environ.get('ACCESS_TOKEN'))


@app.route('/bank_recipient', methods=['POST'])
def bank_recipient():
    bank_account_number = request.form['bank-account-number']
    bank_account_name = request.form['bank-account-name']
    bank_branch_ref = request.form['bank-branch-ref']
    settlement_method = request.form['settlement-method']

    k2connect.initialize(environ['CLIENT_ID'], environ['CLIENT_SECRET'], 'http://127.0.0.1:3000/')
    pay_service = k2connect.Pay

    bank_recipient_request = {
        "access_token": environ.get('ACCESS_TOKEN'),
        "recipient_type": 'bank_account',
        "account_name": bank_account_name,
        "bank_branch_ref": bank_branch_ref,
        "account_number": bank_account_number,
        "settlement_method": settlement_method
    }

    bank_transaction_location = pay_service.add_pay_recipient(bank_recipient_request)
    return render_template('pay_recipient.html', resource_location_url=bank_transaction_location)


@app.route('/mobile_recipient', methods=['POST'])
def mobile_recipient():
    mobile_wallet_first_name = request.form['mobile-wallet-first-name']
    mobile_wallet_last_name = request.form['mobile-wallet-last-name']
    mobile_wallet_network = request.form['mobile-wallet-network']
    mobile_wallet_phone = request.form['mobile-wallet-phone']
    mobile_wallet_email = request.form['mobile-wallet-email']

    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    pay_service = k2connect.Pay

    mobile_recipient_request = {
        "access_token": environ.get('ACCESS_TOKEN'),
        "recipient_type": 'mobile_wallet',
        "first_name": mobile_wallet_first_name,
        "last_name": mobile_wallet_last_name,
        "phone": mobile_wallet_phone,
        "network": mobile_wallet_network,
        "email": mobile_wallet_email
    }

    mobile_transaction_location = pay_service.add_pay_recipient(mobile_recipient_request)
    return render_template('pay_recipient.html', resource_location_url=mobile_transaction_location)


@app.route('/create_payment', methods=['POST'])
def create_payment():
    destination_type = request.form['destination-type']
    destination_reference = request.form['destination-reference']
    amount = request.form['amount']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    pay_service = k2connect.Pay

    metadata = {"sth": "metasth", "last_sth": "another"}
    pay_request = {
        "access_token": environ.get('ACCESS_TOKEN'),
        "destination_reference": destination_reference,
        "destination_type": destination_type,
        "callback_url": 'http://127.0.0.1:5000/result/payment/outgoing',
        "amount": amount,
        "currency": 'KES',
        "metadata": metadata
    }

    create_pay_location = pay_service.send_pay(pay_request)
    return render_template('payment.html', resource_location_url=create_pay_location)


@app.route('/incoming_payment', methods=['POST'])
def incoming_payment():
    payment_channel = request.form['payment-channel']
    till_identifier = request.form['till-identifier']
    stk_first_name = request.form['stk-first-name']
    stk_last_name = request.form['stk-last-name']
    stk_phone = request.form['stk-phone']
    stk_amount = request.form['stk-amount']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    stk_service = k2connect.ReceivePayments

    stk_push_request = {
        "access_token": environ.get('ACCESS_TOKEN'),
        "callback_url": 'http://127.0.0.1:5000/result/payment/incoming',
        "first_name": stk_first_name,
        "last_name": stk_last_name,
        "email": "daivd.j.kariuki@gmail.com",
        "payment_channel": payment_channel,
        "phone_number": stk_phone,
        "till_number": till_identifier,
        "amount": stk_amount
    }

    stk_push_location = stk_service.create_payment_request(stk_push_request)
    return render_template('payment.html', resource_location_url=stk_push_location)


@app.route('/settlment_bank_accounts', methods=['POST'])
def create_settlement_bank_account():
    account_name = request.form['account-name']
    account_number = request.form['account-number']
    settlement_bank_id = request.form['settlement-bank-id']
    settlement_bank_branch_id = request.form['settlement-bank-branch-id']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    transfer_service = k2connect.Transfers
    settlement_bank_location_url = transfer_service.add_bank_settlement_account(environ.get('ACCESS_TOKEN'),
                                                                                account_name, account_number,
                                                                                settlement_bank_id,
                                                                                settlement_bank_branch_id)
    return render_template('settlements.html', resource_location_url=settlement_bank_location_url)


@app.route('/settlment_wallet_accounts', methods=['POST'])
def create_settlement_mobile_account():
    msisdn = request.form['msisdn']
    network = request.form['network']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    transfer_service = k2connect.Transfers
    settlement_mobile_location_url = transfer_service.add_mobile_wallet_settlement_account(environ.get('ACCESS_TOKEN'),
                                                                                           msisdn, network)
    return render_template('settlements.html', resource_location_url=settlement_mobile_location_url)


@app.route('/blind_transfer', methods=['POST'])
def blind_transfer():
    blind_transfer_amount = request.form['blind-transfer-amount']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    transfer_service = k2connect.Transfers
    transfer_location_url = transfer_service.settle_funds(environ.get('ACCESS_TOKEN'),
                                                          'http://127.0.0.1:5000/result/payment/transfer',
                                                          blind_transfer_amount)
    return render_template('transfers.html', resource_location_url=transfer_location_url)


@app.route('/target_transfer', methods=['POST'])
def target_transfer():
    destination_type = request.form['destination-type']
    destination_reference = request.form['destination-reference']
    transfer_amount = request.form['transfer-amount']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    transfer_service = k2connect.Transfers
    transfer_location_url = transfer_service.settle_funds(environ.get('ACCESS_TOKEN'),
                                                          'http://127.0.0.1:5000/result/payment/transfer',
                                                          transfer_amount, destination_type, destination_reference)
    return render_template('transfers.html', resource_location_url=transfer_location_url)


@app.route('/subscription', methods=['POST'])
def subscription():
    webhook_event = request.form['select-webhook-type']
    scope = request.form['scope']
    scope_reference = request.form['scope-reference']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), 'http://127.0.0.1:3000/')
    webhook_service = k2connect.Webhooks

    webhook_request = {
        "access_token": environ.get('ACCESS_TOKEN'),
        "event_type": webhook_event,
        "webhook_endpoint": 'http://127.0.0.1:5000/result/webhook',
        "scope": scope
    }
    if webhook_event in ['b2b_transaction_received', 'buygoods_transaction_received', 'buygoods_transaction_reversed']:
        webhook_request.update({"scope_reference": scope_reference})

    webhook_sub = webhook_service.create_subscription(webhook_request)
    return render_template('webhook_subscription.html', webhook=webhook_sub)


@app.route('/result/webhook', methods=['POST'])
def process_webhook():
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'),
                         'http://127.0.0.1:3000/', environ.get('API_SECRET'))
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    print("Webhook ID: ", decomposed_result.id)
    # get first name
    if decomposed_result.topic == "buygoods_transaction_received":
        print("First Name: ", decomposed_result.first_name)
    elif decomposed_result.topic == "b2b_transaction_received":
        print("Sending Till: ", decomposed_result.sending_till)
    elif decomposed_result.topic == "buygoods_transaction_reversed":
        print("First Name: ", decomposed_result.first_name)
    elif decomposed_result.topic == "m2m_transaction_received":
        print("Sending Merchant: ", decomposed_result.sending_merchant)
    elif decomposed_result.topic == "customer_created":
        print("First Name: ", decomposed_result.first_name)
    elif decomposed_result.topic == "settlement_transfer_completed":
        print("Destination Type: ", decomposed_result.destination_type)
    decomposed_result_hash = json.dumps(decomposed_result, default=lambda o: o.__dict__)
    # print("Decomposed Object: ", decomposed_result_hash)
    return decomposed_result_hash


@app.route('/result/payment/outgoing', methods=['POST'])
def process_pay():
    k2connect.initialize('16D80-Mm-WzRyxbCmUl357XgkczszkLtw5fZc8A17j4', 'OgHgvFGjL2UUcgqHW08he6P-aE8zrRvngdPDuU6Uz0o',
                         'http://127.0.0.1:3000/')
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    # print("Destination: ", decomposed_result.destination)
    return json.dumps(decomposed_result, default=lambda o: o.__dict__)


@app.route('/result/payment/incoming', methods=['POST'])
def process_stk():
    k2connect.initialize('16D80-Mm-WzRyxbCmUl357XgkczszkLtw5fZc8A17j4', 'OgHgvFGjL2UUcgqHW08he6P-aE8zrRvngdPDuU6Uz0o',
                         'http://127.0.0.1:3000/')
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    # print("Transaction Reference: ", decomposed_result.transaction_ref)
    return json.dumps(decomposed_result, default=lambda o: o.__dict__)


@app.route('/result/payment/transfer', methods=['POST'])
def process_transfer():
    k2connect.initialize('16D80-Mm-WzRyxbCmUl357XgkczszkLtw5fZc8A17j4', 'OgHgvFGjL2UUcgqHW08he6P-aE8zrRvngdPDuU6Uz0o',
                         'http://127.0.0.1:3000/')
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    decomposed_result_hash = json.dumps(decomposed_result, default=lambda o: o.__dict__)
    print("Destination Type: ", decomposed_result.destination_type)
    # print("Decomposed Object: ", decomposed_result_hash)
    return decomposed_result_hash


if __name__ == '__main__':
    app.run()
