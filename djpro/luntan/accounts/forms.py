# -*- coding: utf-8 -*-
#
# @file    :forms.py
# @author  :wmjtxt(972213032@qq.com)
# @date    :2020-04-20 20:31:03
# @quote   :
#

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
