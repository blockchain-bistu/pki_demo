#！/usr/bin/env python
# _*_ coding:utf-8 _*_
#cyy
from django.urls import re_path

from . import views
from django.conf.urls import url


urlpatterns = [

    url(r'^index1/', views.index1),
    url(r'^index/', views.index),
    url(r'^zhuce/', views.zhuce),
    url(r'^denglu/', views.denglu),
    url(r'^modify/', views.modify),
    url(r'^del_user/', views.del_user),
    url(r'^upd_user/', views.upd_user),
    url(r'^cha_user/', views.cha_user),
    url(r'^renzheng_user/', views.renzheng_user),
    url(r'^sig/', views.jiami),
    url(r'^jiami/', views.jiami),
    url(r'^luyou/', views.luyou),
     # 下载用户信息文档cyy
    re_path('^DownLoad/', views.DownLoad),
    url(r'^usr_sign/', views.usr_sign),
    url(r'^usr_keypair/', views.usr_keypair),

]
#cyy