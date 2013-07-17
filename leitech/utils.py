#!/usr/bin/env python
# encoding: utf-8
"""
utils.py

Criado por Luan Fonseca em 17/06/2013.
"""

from django.utils import timezone
from django.core.mail import send_mail


def now():
    return timezone.now()