#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence_status.py

Criado por Luan Fonseca em 17/08/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.occurrence_status',
	url(
        regex=r'^occurrence/status/?$', 
        view='list', 
        name='occurrence_status_list'
    ),
    url(
        regex=r'^occurrence/status/add/?$', 
        view='add', 
        name='occurrence_status_add'
    ),
    url(
        regex=r'^occurrence/status/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='occurrence_status_edit'
    ),
    url(
        regex=r'^occurrence/status/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='occurrence_status_delete'
    ),
)