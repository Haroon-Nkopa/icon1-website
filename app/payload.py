import hashlib
import urllib.parse
def generate_payfast_signature(payload, passphrase=None):

    sorted_items = sorted(payload.items())
    # Build the query string
    query_string = urllib.parse.urlencode(sorted_items)
    if passphrase:
        query_string += f'&passphrase={urllib.parse.quote_plus(passphrase)}'
    # Generate MD5 hash
    signature = hashlib.md5(query_string.encode('utf-8')).hexdigest()
    return signature

from flask import current_app

def generate_payfast_payload(form):

    payload = {
        'merchant_id': current_app.config.get('PAYFAST_MERCHANT_ID'),
        'merchant_key': current_app.config.get('PAYFAST_MERCHANT_KEY'),
        'return_url': current_app.config.get('PAYFAST_RETURN_URL'),
        'cancel_url': current_app.config.get('PAYFAST_CANCEL_URL'),
        'notify_url': current_app.config.get('PAYFAST_NOTIFY_URL'),
        'name_first': getattr(form, 'name_first', None) and form.name_first.data or '',
        'name_last': getattr(form, 'name_last', None) and form.name_last.data or '',
        'email_address': getattr(form, 'email_address', None) and form.email_address.data or '',
        'amount': getattr(form, 'amount', None) and form.amount.data or '',
        'item_name': current_app.config.get('PAYFAST_ITEM_NAME', 'Payment'),
    }

    passphrase = current_app.config.get('PAYFAST_PASSPHRASE')
    payload['signature'] = generate_payfast_signature(payload, passphrase)


    return payload