"""
创建时间 : 2018/06/07
版本号 : V1
文档名 : response.py
编辑人 : he_wm
作 用 : 自定义返回值
源存储位置 : \\TmSccity_models\\utils\\response.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""


class BaseResponse(object):

    def __init__(self):
        self.code = 1000
        self.data = None
        self.error = None
        self.token =None

    @property
    def dict(self):
        return self.__dict__
