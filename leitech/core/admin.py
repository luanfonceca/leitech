#!/usr/bin/env python
# encoding: utf-8
u"""
models.py

Criado por Luan Fonseca em 17/06/2013.
"""

from django.contrib import admin
from django.contrib.auth.models import Permission, Group

from core.models import User

admin.site.register(User)
admin.site.register(Permission)