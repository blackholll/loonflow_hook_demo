import hashlib
import time
from django.conf import settings


class CommonService(object):
    @staticmethod
    def check_signature(timestamp, signature):
        """
        校验签名信息
        :param timestamp:
        :param signature:
        :return:
        """
        token = settings.TOKEN
        ori_str = timestamp + token
        tar_str = hashlib.md5(ori_str.encode(encoding='utf-8')).hexdigest()
        if tar_str == signature:
            # The validity of the signature: 120s
            time_now_int = int(time.time())
            if abs(time_now_int - int(timestamp)) <= 120:
                # if abs(time_now_int - int(timestamp)) <= 12000000000000000:
                return True, ''
            else:
                msg = 'The signature you provide in request header is expire, please ensure in 120s'
        else:
            msg = 'The signature you provide in request header is invalid'
        return False, msg

    @staticmethod
    def gen_signature(token):
        """
        生成签名
        :param token:
        :return:
        """
        import time
        timestamp = str(int(time.time()))
        ori_str = timestamp + token
        signature = hashlib.md5(ori_str.encode(encoding='utf-8')).hexdigest()
        return timestamp, signature

