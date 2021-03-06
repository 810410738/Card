"""Card URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='home'),                   # 主页
    url(r'^index/$', views.index, name='index'),            # 主页
    url(r'^login/$', views.login, name='login'),            # 登陆页面
    url(r'^register/$', views.register, name='register'),   # 注册页面
    url(r'^leave/$', views.leave, name='leave'),            # 退出处理
    url(r'^(?P<card_id>[\d]+)/$', views.card, name='card'),     # 名片页面
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^messages/$', views.messages, name='messages'),

]
