from .type import SignType
from .core import Core
class wechatpay():
    def __init__(self, sp_appid, sp_mchid, sub_mchid,description, out_trade_no, notify_url, amount, sp_openid, ):
        """初始化微信支付类
        :param sp_appid: 商户appid
        :param sp_mchid: 商户号
        :param sub_mchid: 子商户号
        :param description: 商品描述
        :param out_trade_no: 商户订单号
        :param notify_url: 异步通知地址
        """
        self.sp_appid = sp_appid
        self.sp_mchid = sp_mchid
        self.sub_mchid = sub_mchid
        self.description = description
        self.out_trade_no = out_trade_no
        self.notify_url = notify_url
        self.sign_type = SignType.MD5


    def sign(self, data, sign_type=SignType.MD5):
        """使用RSAwithSHA256或HMAC_256算法计算签名值供调起支付时使用
        :param data: 需要签名的参数清单
        :微信支付订单采用RSAwithSHA256算法时，示例值:['wx888','1414561699','5K8264ILTKCH16CQ2502S....','prepay_id=wx201410272009395522657....']
        :微信支付分订单采用HMAC_SHA256算法时，示例值:{'mch_id':'1230000109','service_id':'88888888000011','out_order_no':'1234323JKHDFE1243252'}
        """
        return self._core.sign(data, sign_type)
