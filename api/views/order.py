"""
创建时间 : 2018/06/11
版本号 : V1
文档名 : 
编辑人 : he_wm
作 用 : 支付界面
源存储位置 : \\TmSccity_models\\api\\views\\order.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from utils.auth import TmAuth
from django.conf import settings
from django_redis import get_redis_connection
import json
from utils.response import BaseResponse
from api import models
import datetime


class OrderViewSet(APIView):
    # 引入redis
    conn = get_redis_connection("default")
    # 引入登录验证
    authentication_classes = [TmAuth, ]
    # 引入自定义错误类
    ret = BaseResponse()

    def post(self, request, *args, **kwargs):
        """
        立即支付
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 1.获取用户提交数据
        # {
        #     balance: 1000,
        #     money: 900
        # }

        balance = int(request.data.get("balance"))
        money = int(request.data.get("money"))
        # 2.数据验证
        # - 大于等于0
        # - 个人账户是否有1000贝里
        if request.auth.user.balance < balance:
            self.ret.code = 1001
            self.ret.error = '账户TM币余额不足'
#         去结算中心获取课程信息
        course_list = []
        redis_pay_key = settings.PAY_KEY.format(request.auth.user_id, '*', )
        redis_global_coupon_key = settings.PAYMENT_COUPON_KEY.format(request.auth.user_id, )
        for key in self.conn.scan_iter(redis_pay_key,count=10):
            info ={}
            data = self.conn.hgetall(key)
            for k, v in data.items():
                ks = k.decode('utf-8')
                if ks == 'coupon':
                    info[ks] = json.loads(v.decode('utf-8'))
                else:
                    info[ks] = v.decode('utf-8')
            course_list.append(info)
            global_coupon_dict = {
                'coupon': json.loads(self.conn.hget(redis_global_coupon_key, 'coupon').decode('utf-8')),
                'default_coupon': self.conn.hget(redis_global_coupon_key, 'default_coupon').decode('utf-8')
            }
            shopping_car = {"course_list":course_list,"global_coupon_dict":global_coupon_dict}
            self.ret.code = 1000
            self.ret.data = shopping_car
        return Response(self.ret.dict)

