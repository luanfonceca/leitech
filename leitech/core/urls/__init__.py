#!/usr/bin/env python
# encoding: utf-8
u"""
__init__.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^', include('core.urls.occurrence_type')),
	url(r'^', include('core.urls.occurrence_status')),
	url(r'^', include('core.urls.occurrence')),
)