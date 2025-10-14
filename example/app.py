import json

from flask import Flask, render_template, request
import k2connect
import datetime
from os import environ
from k2connect import payload_decomposer

app = Flask(__name__)
app.debug = True

BASE_URL = "https://staging.kopokopo.com/"
CALLBACK_URL = "https://webhook.site/a1f866a4-284c-46cb-ad76-83df81b0c053"


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

    k2connect.initialize(environ['CLIENT_ID'], environ['CLIENT_SECRET'], BASE_URL)
    token_service = k2connect.Tokens
    access_token_response = token_service.request_access_token()
    environ['ACCESS_TOKEN'] = token_service.get_access_token(access_token_response)

    return render_template('token.html', client_id=environ.get('CLIENT_ID'), client_secret=environ.get('CLIENT_SECRET'),
                           given_time=given_time, access_token=environ.get('ACCESS_TOKEN'))


@app.route('/send_money', methods=['POST'])
def send_money():
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), BASE_URL)
    send_money_service = k2connect.SendMoney(access_token=environ.get('ACCESS_TOKEN'))
    destination_request = _build_send_money_request()

    send_money_request = {
        "destinations": [destination_request],
        "callback_url": CALLBACK_URL,
        "source_identifier": None,
        "currency": "KES"
    }

    send_money_location = send_money_service.create_payment(send_money_request)
    return render_template('send_money.html', resource_location_url=send_money_location)


@app.route('/add_external_recipient', methods=['POST'])
def add_external_recipient():
    external_recipient_request = _build_external_recipient_request()
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), BASE_URL)
    send_money_service = k2connect.SendMoney(access_token=environ.get('ACCESS_TOKEN'))

    add_send_money_recipient_location = send_money_service.add_external_recipient(external_recipient_request)
    return render_template('send_money.html', resource_location_url=add_send_money_recipient_location)


@app.route('/query_send_money_payment', methods=['POST'])
def query_send_money_payment():
    resource_url = request.form['resource-url']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), BASE_URL)
    send_money_service = k2connect.SendMoney(access_token=environ.get('ACCESS_TOKEN'))

    send_money_resource_location = send_money_service.query_resource(resource_url)
    return render_template('payment.html', resource_location_url=send_money_resource_location)


@app.route('/merchant_transfer_account', methods=['POST'])
def create_merchant_transfer_account():
    transfer_account_request = _build_transfer_account_request()
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), BASE_URL)
    transfer_service = k2connect.TransferAccount(access_token=access_token)
    transfer_account_location_url = transfer_service.add_transfer_account(transfer_account_request)
    return render_template('settlements.html', resource_location_url=transfer_account_location_url)


@app.route('/subscription', methods=['POST'])
def subscription():
    webhook_event = request.form['select-webhook-type']
    scope = request.form['scope']
    scope_reference = request.form['scope-reference']
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'), BASE_URL)
    webhook_service = k2connect.Webhooks(access_token=environ.get('ACCESS_TOKEN'), )

    webhook_request = {
        "event_type": webhook_event,
        "url": CALLBACK_URL,
        "scope": scope
    }
    if scope == 'till':
        webhook_request.update({"scope_reference": scope_reference})

    webhook_sub = webhook_service.create_subscription(webhook_request)
    return render_template('webhook_subscription.html', webhook=webhook_sub)


@app.route('/result/webhook', methods=['POST'])
def process_webhook():
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'),
                         BASE_URL, environ.get('API_SECRET'))
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
    return decomposed_result_hash


@app.route('/result/payment/outgoing', methods=['POST'])
def process_pay():
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'),
                         BASE_URL)
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    return json.dumps(decomposed_result, default=lambda o: o.__dict__)


@app.route('/result/payment/incoming', methods=['POST'])
def process_stk():
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'),
                         BASE_URL)
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    return json.dumps(decomposed_result, default=lambda o: o.__dict__)


@app.route('/result/payment/transfer', methods=['POST'])
def process_transfer():
    k2connect.initialize(environ.get('CLIENT_ID'), environ.get('CLIENT_SECRET'),
                         BASE_URL)
    result_handler = k2connect.ResultHandler
    processed_payload = result_handler.process(request)
    decomposed_result = payload_decomposer.decompose(processed_payload)
    decomposed_result_hash = json.dumps(decomposed_result, default=lambda o: o.__dict__)
    print("Destination Type: ", decomposed_result.destination_type)
    return decomposed_result_hash


def _build_send_money_request():
    destination_type = request.form["destination_type"]
    if destination_type == "mobile_wallet":
        return {
            "type": destination_type,
            "nickname": request.form["nickname"],
            "phone_number": request.form["phone_number"],
            "network": request.form["network"],
            "amount": request.form["amount"],
            "description": request.form["description"],
            "favourite": False
        }
    elif destination_type == "bank_account":
        return {
            "type": destination_type,
            "nickname": request.form["nickname"],
            "account_name": request.form["account_name"],
            "account_number": request.form["account_number"],
            "bank_branch_ref": request.form["bank_branch_ref"],
            "amount": request.form["amount"],
            "description": request.form["description"],
            "favourite": False
        }
    elif destination_type == "paybill":
        return {
            "type": destination_type,
            "nickname": request.form["nickname"],
            "paybill_number": request.form["paybill_number"],
            "paybill_account_number": request.form["paybill_account_number"],
            "amount": request.form["amount"],
            "description": request.form["description"],
            "favourite": False
        }
    elif destination_type == "till":
        return {
            "type": destination_type,
            "nickname": request.form["nickname"],
            "till_number": request.form["till_number"],
            "amount": request.form["amount"],
            "description": request.form["description"],
            "favourite": False
        }
    elif destination_type == "merchant_wallet":
        return {
            "type": request.form["destination_type"],
            "reference": request.form["reference"],
            "amount": request.form["amount"],
        }
    elif destination_type == "merchant_bank_account":
        return {
            "type": request.form["destination_type"],
            "reference": request.form["reference"],
            "amount": request.form["amount"],
        }
    else:
        raise ValueError("Invalid destination type")


def _build_external_recipient_request():
    recipient_type = request.form['recipient_type']
    if recipient_type == "mobile_wallet":
        return {
            "type": recipient_type,
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "phone_number": request.form["phone_number"],
            "email": request.form["email"],
            "nickname": request.form["nickname"],
            "network": request.form["network"],
        }
    elif recipient_type == "bank_account":
        return {
            "type": recipient_type,
            "account_name": request.form["account_name"],
            "account_number": request.form["account_number"],
            "bank_branch_ref": request.form["bank_branch_ref"],
            "nickname": request.form["nickname"],
        }
    elif recipient_type == "paybill":
        return {
            "type": recipient_type,
            "paybill_name": request.form["paybill_name"],
            "paybill_number": request.form["paybill_number"],
            "paybill_account_number": request.form["paybill_account_number"],
            "nickname": request.form["nickname"],
        }
    elif recipient_type == "till":
        return {
            "type": recipient_type,
            "till_name": request.form["till_name"],
            "till_number": request.form["till_number"],
            "nickname": request.form["nickname"],
        }
    else:
        raise ValueError("Invalid recipient type")


def _build_transfer_account_request():
    transfer_account_type = request.form['recipient_type']
    if transfer_account_type == "merchant_bank_account":
        return {
            "type": transfer_account_type,
            "account_name": request.form["account_name"],
            "account_number": request.form["account_number"],
            "bank_branch_ref": request.form["bank_branch_ref"],
            "settlement_method": request.form["settlement_method"],
            "nickname": request.form["nickname"],
        }
    elif transfer_account_type == "merchant_wallet":
        return {
            "type": transfer_account_type,
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "phone_number": request.form["phone_number"],
            "email": request.form["email"],
            "network": request.form["network"],
            "nickname": request.form["nickname"],
        }
    else:
        raise ValueError("Invalid recipient type")


if __name__ == '__main__':
    app.run()
