from .type import SignType
from .core import Core
class wechatpay():
    def __init__(self, appid, mch_id, key, sub_mch_id, notify_url, trade_type='JSAPI'):
        self.appid = appid
        self.mch_id = mch_id
        self.key = key
        self.sub_mch_id = sub_mch_id
        self.notify_url = notify_url
        self.trade_type = trade_type
        self._core = Core(mch_id, key,"cert_dir","apiv3_key")

    def sign(self, data, sign_type=SignType.MD5):
        """使用RSAwithSHA256或HMAC_256算法计算签名值供调起支付时使用
        :param data: 需要签名的参数清单
        :微信支付订单采用RSAwithSHA256算法时，示例值:['wx888','1414561699','5K8264ILTKCH16CQ2502S....','prepay_id=wx201410272009395522657....']
        :微信支付分订单采用HMAC_SHA256算法时，示例值:{'mch_id':'1230000109','service_id':'88888888000011','out_order_no':'1234323JKHDFE1243252'}
        """
        return self._core.sign(data, sign_type)
