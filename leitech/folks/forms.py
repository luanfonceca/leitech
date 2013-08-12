#!/usr/bin/env python
# encoding: utf-8
u"""
forms.py

Criado por Luan Fonseca em 08/08/2013.
"""

from django import forms

from folks.models import *
from utils import HistoryModelForm

class PoliceCarForm(HistoryModelForm):
    class Meta:
        model = PoliceCar


class PoliceForm(HistoryModelForm):
    class Meta:
        model = Police


class SchoolForm(HistoryModelForm):
    class Meta:
        model = School


class AttendedPublicForm(HistoryModelForm):
    class Meta:
        model = AttendedPublic


class AddressForm(HistoryModelForm):
    class Meta:
        model = Address
