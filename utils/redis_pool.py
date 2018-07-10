"""
创建时间 : 2018/06/07
版本号 : V1
文档名 : redis_pool.py
编辑人 : he_wm
作 用 : 单例模式redis链接
源存储位置 : \\TmSccity_models\\utils\\redis_pool.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""
# !/usr/bin/env python
# _*_ coding:utf-8 _*_
from django_redis import get_redis_connection

conn = get_redis_connection()
