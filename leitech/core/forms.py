#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django import forms

from core.models import *
from utils import HistoryModelForm

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


class AttendedPublicForm(HistoryModelForm):
    class Meta:
        model = AttendedPublic


class AddressForm(HistoryModelForm):
    class Meta:
        model = Address
