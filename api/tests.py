from django.test import TestCase

# from api.models import *
# from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# from django.contrib.contenttypes.models import ContentType
# Create your tests here.


import redis
#
conn = redis.Redis(host='192.168.131.129', port=6379, password='123456')
# # 清空操作
# conn.flushall()
# # 打印所有数据
print(conn.keys())
# print(conn.hgetall('shopping_car_key_1_1'))
# print(conn.hgetall('pay_key_1_1'))
# print(conn.hgetall('payment_coupon_key_1'))


# lis = [1, 2, 3, 4, 5, 6, 44, 66, 77]
# sum = 0
# for i in range(0,len(lis)-1):
#     if sum >= 100:
#         break
#     sum += lis[i]
#     print(lis[i])
# print(sum)

