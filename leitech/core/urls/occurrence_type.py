#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence_type.py

Criado por Luan Fonseca em 19/06/2013.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views.occurrence_type',
    url(
        regex=r'^occurrence/types/?$', 
        view='list', 
        name='occurrence_type_list'
    ),
    url(
        regex=r'^occurrence/type/add/?$', 
        view='add', 
        name='occurrence_type_add'
    ),
    url(
        regex=r'^occurrence/type/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='occurrence_type_edit'
    ),
    url(
        regex=r'^occurrence/type/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='occurrence_type_delete'
    ),
)