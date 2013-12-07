#!/usr/bin/env python
# encoding: utf-8
u"""
__init__.py

Criado por Luan Fonseca em 09/09/2013.
"""

from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
	url(r'^', include('folks.urls.police')),
	url(r'^', include('folks.urls.police_car')),
	url(r'^', include('folks.urls.school')),
	url(r'^', include('folks.urls.attended_public')),
	# url(r'^', include('folks.urls.address')),
)