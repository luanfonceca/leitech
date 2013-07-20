#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django import forms

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

