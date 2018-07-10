"""
创建时间 : 2018/06/04
版本号 : V1
文档名 : newspapers
编辑人 : he_wm
作 用 : 新闻板块接口
源存储位置 : TmSccity_models\api\views\course\coursehost.py
修改及增加功能记录 :
    修改时间 : 
        1、2018/04/02:
        2、
    增加功能时间 :
        1、
        2、   
"""

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSetMixin

from api.models import *
from utils.auth import TmAuth
from utils.response import BaseResponse
from api.serializers.coursehost import *


class NewsPapers(ViewSetMixin, APIView):
    authentication_classes = [TmAuth, ]
    ret = BaseResponse()

    def list(self, request, *args, **kwargs):
        """
        新闻主页显示
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # ret = BaseResponse()
        # ret = {'code': 1000, 'data': None}
        try:
            queryset = Article.objects.all()
            ser = ArticleViewSetSerializers(instance=queryset, many=True)
            self.ret.data = ser.data
        except Exception as e:
            self.ret.code = 1001
            self.ret.error = '未获取到资源'
        return Response(self.ret.dict)

    def retrieve(self, request, *args, **kwargs):
        # ret = BaseResponse()
        try:
            pk = kwargs.get('pk')
            obj = Article.objects.filter(pk=pk).first()
            ser = ArticleDetailViewSetSerializers(instance=obj, many=False)
            self.ret.data = ser.data
        except Exception as e:
            self.ret.code = 1001
            self.ret.error = '未获取到资源'
        return Response(self.ret.dict)


class AgreeView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        """
        列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def post(self, request, *args, **kwargs):
        """
        点赞
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = Article.objects.filter(id=pk).first()
            obj.agree_num = obj.agree_num + 1
            obj.save()
            self.ret.data = obj.agree_num
        except Exception as e:
            self.ret.code = 1001
            self.ret.error = '点赞失败'
        return Response(self.ret.dict)
