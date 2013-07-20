#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views.occurrence',
	url(
        regex=r'^occurrences/?$', 
        view='list', 
        name='occurrence_list'
    ),
    url(
        regex=r'^occurrence/add/?$', 
        view='add', 
        name='occurrence_add'
    ),
    url(
        regex=r'^occurrence/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='occurrence_edit'
    ),
    url(
        regex=r'^occurrence/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='occurrence_delete'
    ),
)