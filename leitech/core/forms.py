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
        exclude = ['seized_materials']
        order = [
            'nature', 'relevant_information',
            'attended_public', 'state', 'city',
            'neighborhood', 'zipcode', 'street',
            'complement', 'number', 'region',
            'school', 'type', 'police_car',
            'description', 'seized_materials',
        ]
