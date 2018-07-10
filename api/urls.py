from django.conf.urls import url

from api.views.user import account
from api.views.course import coursehost
from api.views.course import newspapers
from api.views.shopping import shoppings

urlpatterns = [
    # 登录
    url(r'^login/$', account.loginView.as_view()),
    # 课程相关
    url(r'^course/$', coursehost.CourseViewSet.as_view({"get": "list"})),
    url(r'^course/(?P<pk>\d+)/$', coursehost.CourseViewSet.as_view({"get": "retrieve"})),
    # 新闻相关
    url(r'^newspapers/$', newspapers.NewsPapers.as_view({"get": "list"})),
    url(r'^newspapers/(?P<pk>\d+)/$', newspapers.NewsPapers.as_view({"get": "retrieve"})),
    url(r'^newspapers/(?P<pk>\d+)/agree/$', newspapers.AgreeView.as_view({'post': 'post'})),
    #     购物车相关
    url(r'^shoppingcar/$', shoppings.Shoppings.as_view()),
    url(r'^check_out/$', shoppings.Check_out.as_view()),
]



















