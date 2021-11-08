SAMPLE_CLIENT_ID = 'T1RyrPntqO4PJ35RLv6IVfPKRyg6gVoMvXEwEBin9Cw'
SAMPLE_CLIENT_SECRET = 'Ywk_J18RySqLOmhhhVm8fhh4FzJTUzVcZJ03ckNpZK8'
SAMPLE_WEBHOOK_SECRET = 'sample_webhook_secret'
SAMPLE_BASE_URL = 'https://sandbox.kopokopo.com/'
SAMPLE_BEARER_TOKEN = 'Z9tnzpV-zwdk2ezCX-cBYLV4afcYfgl79NpjeNgfDQI'
SAMPLE_AUTHORIZATION_PATH = '/oauth/token'
SAMPLE_DICTIONARY = {
    'amount': '50,000',
    'currency': 'KSh'
}

MOBILE_PAY_RECIPIENT = {
    "first_name": "mobile_wallet_first_name",
    "last_name": "mobile_wallet_last_name",
    "phone_number": "+254123456789",
    "network": "mobile_wallet_network",
    "email": "test@test.com"
}

INVALID_FIRST_NAME_MOBILE_PAY_RECIPIENT = {
    "last_name": "mobile_wallet_last_name",
    "phone_number": "+254123456789",
    "network": "mobile_wallet_network",
    "email": "test@test.com"
}

INVALID_EMAIL_MOBILE_PAY_RECIPIENT = {
    "first_name": "mobile_wallet_first_name",
    "last_name": "mobile_wallet_last_name",
    "phone_number": "+254123456789",
    "network": "mobile_wallet_network",
    "email": "mobile_wallet_email"
}

INVALID_PHONE_MOBILE_PAY_RECIPIENT = {
    "first_name": "mobile_wallet_first_name",
    "last_name": "mobile_wallet_last_name",
    "phone_number": "mobile_wallet_phone",
    "network": "mobile_wallet_network",
    "email": "test@test.com"
}

BANK_PAY_RECIPIENT = {
    "settlement_method": "EFT",
    "account_name": "bank_account_name",
    "bank_branch_ref": "633aa26c-7b7c-4091-ae28-96c0687cf886",
    "account_number": "bank_account_number"
}

BANK_PAY_RECIPIENT_RTS = {
    "settlement_method": "RTS",
    "account_name": "bank_account_name",
    "bank_branch_ref": "633aa26c-7b7c-4091-ae28-96c0687cf886",
    "account_number": "bank_account_number"
}

TILL_PAY_RECIPIENT = {
    "till_name": "Python Test Till",
    "till_number": "519953"
}

INVALID_TILL_NAME_PAY_RECIPIENT = {
    "till_number": "519953"
}

INVALID_TILL_NUMBER_PAY_RECIPIENT = {
    "till_name": "Python Test Till",
}

PAYBILL_PAY_RECIPIENT = {
    "paybill_name": "Python Payhiss",
    "paybill_number": "815581",
    "paybill_account_number": "account_one"
}

INVALID_PAYBILL_NAME_PAYBILL = {
    "paybill_number": "815581",
    "paybill_account_number": "account_one"
}

INVALID_PAYBILL_NUMBER_PAYBILL = {
    "paybill_name": "Python Payhiss",
    "paybill_account_number": "account_one"
}

INVALID_PAYBILL_ACCOUNT_NUMBER_PAYBILL = {
    "paybill_name": "Python Payhiss",
    "paybill_number": "815581",
}

INVALID_FIRST_NAME_BANK_PAY_RECIPIENT = {
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_ref": "21",
    "bank_branch_ref": "633aa26c-7b7c-4091-ae28-96c0687cf886",
    "account_number": "bank_account_number",
    "email": "test@test.com",
    "phone_number": "+254123456789"
}

INVALID_PHONE_BANK_PAY_RECIPIENT = {
    "first_name": "bank_account_recipient_first_name",
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_ref": "21",
    "bank_branch_ref": "633aa26c-7b7c-4091-ae28-96c0687cf886",
    "account_number": "bank_account_number",
    "email": "test@test.com",
    "phone_number": "mobile_phone"
}

INVALID_EMAIL_BANK_PAY_RECIPIENT = {
    "first_name": "bank_account_recipient_first_name",
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_ref": "21",
    "bank_branch_ref": "633aa26c-7b7c-4091-ae28-96c0687cf886",
    "account_number": "bank_account_number",
    "email": "test",
    "phone_number": "+254123456789"
}

PAY = {
    "mobile_pay": MOBILE_PAY_RECIPIENT,
    "invalid_first_name_mobile_pay": INVALID_FIRST_NAME_MOBILE_PAY_RECIPIENT,
    "invalid_email_mobile_pay": INVALID_EMAIL_MOBILE_PAY_RECIPIENT,
    "invalid_phone_mobile_pay": INVALID_PHONE_MOBILE_PAY_RECIPIENT,
    "bank_pay": BANK_PAY_RECIPIENT,
    "invalid_first_name_bank_pay": INVALID_FIRST_NAME_BANK_PAY_RECIPIENT,
    "invalid_phone_bank_pay": INVALID_PHONE_BANK_PAY_RECIPIENT,
    "invalid_email_bank_pay": INVALID_EMAIL_BANK_PAY_RECIPIENT,
    "till_pay": TILL_PAY_RECIPIENT,
    "invalid_till_name_till_pay": INVALID_TILL_NAME_PAY_RECIPIENT,
    "invalid_till_number_till_pay": INVALID_TILL_NUMBER_PAY_RECIPIENT,
    "paybill_pay": PAYBILL_PAY_RECIPIENT,
    "invalid_paybill_name_paybill": INVALID_PAYBILL_NAME_PAYBILL,
    "invalid_paybill_number_paybill": INVALID_PAYBILL_NUMBER_PAYBILL,
    "invalid_paybill_account_number_paybill": INVALID_PAYBILL_ACCOUNT_NUMBER_PAYBILL,
}

MSG = {
    "invalid_phone": "The phone number passed is invalid.",
    "invalid_email": "The email address passed is invalid.",
    "invalid_url_format": "The url format passed is invalid (should be : https://domain.com)",
    "invalid_scheme_cert": "Provide a url with a valid certificate => (http://) or (https://"
}
