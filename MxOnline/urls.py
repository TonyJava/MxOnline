# _*_ coding:utf-8 _*_
"""MxOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import xadmin
#  用来处理静态文件
from django.views.static import serve
#  加载登录视图
from users.views import LoginView,RegisterView, AciveUserView,ForgetPwdView, ResetView,ModifyPwdView
from organization.views import OrgView
from MxOnline.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 首页加载
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # 登录页面
    url(r'^login/$', LoginView.as_view(), name='login'),
    # 注册页面
    url(r'register/$',RegisterView.as_view(), name='register'),
    # 验证码登录
    url(r'^captcha/', include('captcha.urls')),
    # 邮箱激活
    url(r'^active/(?P<active_code>.*)/$',AciveUserView.as_view(),name='user_active'),
    # 忘记密码
    url(r'^forget/$',ForgetPwdView.as_view(),name='forget_pwd'),
    # 重置密码
    url(r'^reset/(?P<active_code>.*)/$',ResetView.as_view(),name='reset_pwd'),
    # 重置密码表单 POST 请求
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace='org')),
    # 课程列表url配置
    url(r'^course/', include('courses.urls', namespace='courses')),


    #  处理上传文件media的信息
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT})




]
