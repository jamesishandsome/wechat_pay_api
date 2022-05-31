from enum import Enum

class SignType(Enum):
    HMAC_SHA256 = 'HMAC-SHA256'
    MD5 = 'MD5'
    RSA_SHA256 = 'RSA-SHA256'
