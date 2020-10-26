SAMPLE_CLIENT_ID = 'ReMYAYdLKcg--XNmKhzkLNTIbXPvOUPs3hyycUF8WmI'
SAMPLE_CLIENT_SECRET = '4707e306330759f4b63716f0525f6634a4685b4b4bf75b3381f1244ee77eb3fa'
SAMPLE_WEBHOOK_SECRET = 'sample_webhook_secret'
SAMPLE_BASE_URL = 'http://127.0.0.1:3000/'
SAMPLE_BEARER_TOKEN = 'Z9tnzpV-zwdk2ezCX-cBYLV4afcYfgl79NpjeNgfDQI'
SAMPLE_AUTHORIZATION_PATH = '/oauth/token'
SAMPLE_DICTIONARY = {
    'amount': '50,000',
    'currency': 'KSh'
}

MOBILE_PAY_RECIPIENT = {
    "first_name": "mobile_wallet_first_name",
    "last_name": "mobile_wallet_last_name",
    "phone": "+254123456789",
    "network": "mobile_wallet_network",
    "email": "test@test.com"
}

INVALID_FIRST_NAME_MOBILE_PAY_RECIPIENT = {
    "last_name": "mobile_wallet_last_name",
    "phone": "+254123456789",
    "network": "mobile_wallet_network",
    "email": "test@test.com"
}

INVALID_EMAIL_MOBILE_PAY_RECIPIENT = {
    "first_name": "mobile_wallet_first_name",
    "last_name": "mobile_wallet_last_name",
    "phone": "+254123456789",
    "network": "mobile_wallet_network",
    "email": "mobile_wallet_email"
}

INVALID_PHONE_MOBILE_PAY_RECIPIENT = {
    "first_name": "mobile_wallet_first_name",
    "last_name": "mobile_wallet_last_name",
    "phone": "mobile_wallet_phone",
    "network": "mobile_wallet_network",
    "email": "test@test.com"
}

BANK_PAY_RECIPIENT = {
    "first_name": "bank_account_recipient_first_name",
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_id": "bank_id",
    "bank_branch_id": "bank_branch_id",
    "account_number": "bank_account_number",
    "email": "test@test.com",
    "phone": "+254123456789"
}

INVALID_FIRST_NAME_BANK_PAY_RECIPIENT = {
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_id": "bank_id",
    "bank_branch_id": "bank_branch_id",
    "account_number": "bank_account_number",
    "email": "test@test.com",
    "phone": "+254123456789"
}

INVALID_PHONE_BANK_PAY_RECIPIENT = {
    "first_name": "bank_account_recipient_first_name",
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_id": "bank_id",
    "bank_branch_id": "bank_branch_id",
    "account_number": "bank_account_number",
    "email": "test@test.com",
    "phone": "mobile_phone"
}

INVALID_EMAIL_BANK_PAY_RECIPIENT = {
    "first_name": "bank_account_recipient_first_name",
    "last_name": "bank_account_recipient_last_name",
    "account_name": "bank_account_name",
    "bank_id": "bank_id",
    "bank_branch_id": "bank_branch_id",
    "account_number": "bank_account_number",
    "email": "test",
    "phone": "+254123456789"
}

PAY = {
    "mobile_pay": MOBILE_PAY_RECIPIENT,
    "invalid_first_name_mobile_pay": INVALID_FIRST_NAME_MOBILE_PAY_RECIPIENT,
    "invalid_email_mobile_pay": INVALID_EMAIL_MOBILE_PAY_RECIPIENT,
    "invalid_phone_mobile_pay": INVALID_PHONE_MOBILE_PAY_RECIPIENT,
    "bank_pay": BANK_PAY_RECIPIENT,
    "invalid_first_name_bank_pay": INVALID_FIRST_NAME_BANK_PAY_RECIPIENT,
    "invalid_phone_bank_pay": INVALID_PHONE_BANK_PAY_RECIPIENT,
    "invalid_email_bank_pay": INVALID_EMAIL_BANK_PAY_RECIPIENT
}

MSG = {
    "invalid_phone": "The phone number passed is invalid.",
    "invalid_email": "The email address passed is invalid.",
    "invalid_url_format": "The url format passed is invalid (should be : https://domain.com)",
    "invalid_scheme_cert": "Provide a url with a valid certificate => (http://) or (https://"
}
