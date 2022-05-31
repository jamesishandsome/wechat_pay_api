import base64
import hashlib
import hmac
def sign_md5(stringSign):
    m = hashlib.md5()
    m.update(stringSign.encode('utf-8'))
    return m.hexdigest().upper()

def sign_hmac_sha256(stringSign, key):
    key = key.encode('utf-8')
    stringSign = stringSign.encode('utf-8')
    sign = hmac.new(key,stringSign, digestmod=hashlib.sha256).hexdigest().upper()
    return sign
