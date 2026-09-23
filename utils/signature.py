import hmac
import hashlib
import base64

def generate_signature(key, message):
    key = key.encode('utf-8')
    message = message.encode('utf-8')

    hmac_sha = hmac.new(key,message,hashlib.sha256)
    digest = hmac_sha.digest()
    signature = base64.b64encode(digest).decode('utf-8')

    return signature