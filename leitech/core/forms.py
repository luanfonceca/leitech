#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django import forms
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import (UserCreationForm, 
                                       PasswordChangeForm, 
                                       SetPasswordForm)
from registration.forms import RegistrationFormUniqueEmail
from registration.models import RegistrationProfile

from core.models import *

class HistoryModelForm(forms.ModelForm):
    def save(self, user, *args, **kwargs):
    	self.instance.updated_by = user
    	if not self.instance.pk:
    		self.instance.created_by = self.instance.updated_by
    	return super(HistoryModelForm, self).save(*args, **kwargs)
    

class SeizedMaterialForm(HistoryModelForm):
    class Meta:
        model = SeizedMaterial


class SeizedMaterialTypeForm(HistoryModelForm):
    class Meta:
        model = SeizedMaterialType


class PoliceCarForm(HistoryModelForm):
    class Meta:
        model = PoliceCar


class PoliceForm(HistoryModelForm):
    class Meta:
        model = Police


class OccurrenceTypeForm(HistoryModelForm):
    class Meta:
        model = OccurrenceType


class SchoolForm(HistoryModelForm):
    class Meta:
        model = School


class OccurrenceForm(HistoryModelForm):
    class Meta:
        model = Occurrence
        exclude = ['seized_materials']


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


class AttendedPublicForm(HistoryModelForm):
    class Meta:
        model = AttendedPublic


class OccurrenceSeizedMaterialForm(forms.ModelForm):
    class Meta:
        model = OccurrenceSeizedMaterial

    def __init__(self, *args, **kwargs):
        super(OccurrenceSeizedMaterialForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'seized_material', 
            'amount',
        ]
    

OSMFormSet = inlineformset_factory(
    parent_model=Occurrence, 
    model=OccurrenceSeizedMaterial,
    form=OccurrenceSeizedMaterialForm,
    can_delete=False,
    extra=1, 
)

class AddressForm(HistoryModelForm):
    class Meta:
        model = Address
