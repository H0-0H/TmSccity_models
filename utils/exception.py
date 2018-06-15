"""
创建时间 : 2018/06/07
版本号 : V1
文档名 : exception.py
编辑人 : he_wm
作 用 : 自定义抛错
源存储位置 : \\TmSccity_models\\utils\\exception.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""


class PricePolicyInvalid(Exception):
    def __init__(self, msg):
        self.msg = msg
