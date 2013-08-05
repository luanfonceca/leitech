#!/usr/bin/env python
# encoding: utf-8
u"""
__init__.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^', include('core.urls.occurrence_type')),
	url(r'^', include('core.urls.occurrence')),
	url(r'^', include('core.urls.police')),
	url(r'^', include('core.urls.police_car')),
	url(r'^', include('core.urls.school')),
	url(r'^', include('core.urls.seized_material')),
	url(r'^', include('core.urls.seized_material_type')),
	url(r'^', include('core.urls.user')),
	url(r'^', include('core.urls.attended_public')),
)