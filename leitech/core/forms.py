#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django import forms

from core.models import *
from utils import HistoryModelForm

class OccurrenceTypeForm(HistoryModelForm):
    class Meta:
        model = OccurrenceType


class OccurrenceStatusForm(HistoryModelForm):
    class Meta:
        model = OccurrenceStatus


class OccurrenceForm(HistoryModelForm):
    class Meta:
        model = Occurrence
        exclude = [u'seized_materials']
        order = [
            u'nature', u'relevant_information',
            u'attended_public', u'state', u'city',
            u'neighborhood', u'zipcode', u'street',
            u'complement', u'number', u'region',
            u'school', u'type', u'police_car',
            u'description', u'seized_materials',
        ]
