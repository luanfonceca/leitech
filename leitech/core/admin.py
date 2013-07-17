#!/usr/bin/env python
# encoding: utf-8
u"""
models.py

Criado por Luan Fonseca em 17/06/2013.
"""

from django.contrib import admin
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType

admin.site.register(Permission)

# Registrando todas os Models da app na Admin.
map(lambda x: 
	admin.site.register(
		x.model_class()
	), ContentType.objects.filter(app_label=__package__)
)
	