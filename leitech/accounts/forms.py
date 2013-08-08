#!/usr/bin/env python
# encoding: utf-8
u"""
forms.py

Criado por Luan Fonseca em 08/08/2013.
"""

from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import (UserCreationForm, 
                                       PasswordChangeForm, 
                                       SetPasswordForm)
from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile

from accounts.models import *
from utils import HistoryModelForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 
                  'email', 'password1',
                  'password2', 'is_manager']
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        del self.fields['username']
        

class UserEditForm(HistoryModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class UserEditPasswordForm(PasswordChangeForm):
    class Meta:
        model = User


class UserResetPasswordForm(SetPasswordForm):
    class Meta:
        model = User