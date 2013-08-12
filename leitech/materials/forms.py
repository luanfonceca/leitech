#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django import forms
from django.forms.models import inlineformset_factory, BaseInlineFormSet

from materials.models import *
from core.models import Occurrence
from utils import HistoryModelForm

class SeizedMaterialForm(HistoryModelForm):
    class Meta:
        model = SeizedMaterial


class SeizedMaterialTypeForm(HistoryModelForm):
    class Meta:
        model = SeizedMaterialType


class OccurrenceSeizedMaterialForm(HistoryModelForm):
    class Meta:
        model = OccurrenceSeizedMaterial
        exclude = ['id']

    def __init__(self, *args, **kwargs):
        super(OccurrenceSeizedMaterialForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'seized_material', 
            'amount',
        ]
    
class OccurrenceSeizedMaterialFormSet(BaseInlineFormSet):
    def save(self, user=None, commit=True):        
        if user:
            self.instance.updated_by = user
            if not self.instance.pk:
                self.instance.created_by = self.instance.updated_by
        return super(OccurrenceSeizedMaterialFormSet, self).save(commit=commit)

OSMFormSet = inlineformset_factory(
    parent_model=Occurrence, 
    model=OccurrenceSeizedMaterial,
    form=OccurrenceSeizedMaterialForm,
    formset=OccurrenceSeizedMaterialFormSet,
    can_delete=False,
    extra=1, 
)