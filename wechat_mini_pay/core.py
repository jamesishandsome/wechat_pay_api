import json
import os
from datetime import datetime
import requests
from .type import SignType
from utils import sign_hmac_sha256,sign_md5,sign_rsa_sha256
class Core():
    def __init__(self,mch_id,key, cert_dir, apiv3_key):
        self.mch_id = mch_id
        self.key = key
        self.cert_dir = cert_dir
        self.apiv3_key = apiv3_key

    def sign(self,data,sign_type):
        if sign_type == SignType.MD5:
            return sign_md5(data)
        elif sign_type == SignType.HMAC_SHA256:
            return sign_hmac_sha256(data)
        elif sign_type == SignType.RSA_SHA256:
            return sign_hmac_sha256(data)
