#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Criado por Luan Fonseca em 17/06/2013.
"""

from django.utils import timezone
from django.core.mail import send_mail
from django import forms


def now():
    return timezone.now()


class HistoryModelForm(forms.ModelForm):
    def save(self, user=None, *args, **kwargs):
        if user:
            self.instance.updated_by = user
            if not self.instance.pk:
                self.instance.created_by = self.instance.updated_by
        return super(HistoryModelForm, self).save(*args, **kwargs)