# _*_ coding:utf-8 _*_
__author__ = 'bobby'
__date__ = '2017/5/18 10:08'
import re

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):

    #  在原来的基础上进行扩展
    # my_filed = forms.CharField
    class Meta:
        #继承  model里面的东西
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']
        # 自定义mobile输入要求
        def clean_mobile(self):
            """
             验证手机号码是否合法
            """
            mobile = self.cleaned_data['mobile']
            REGEX_MOBILE = "^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$"
            p = re.compile(REGEX_MOBILE)
            if p.match(mobile):
                return mobile
            else:
                raise  forms.ValidationError(u'手机号码非法',code = 'mobile_invalid')





