#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django import forms
from django.forms.models import inlineformset_factory

from materials.models import *
from core.models import Occurrence
from utils import HistoryModelForm

class SeizedMaterialForm(HistoryModelForm):
    class Meta:
        model = SeizedMaterial


class SeizedMaterialTypeForm(HistoryModelForm):
    class Meta:
        model = SeizedMaterialType


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