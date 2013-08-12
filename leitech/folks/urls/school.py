#!/usr/bin/env python
# encoding: utf-8
u"""
school.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('folks.views.school',
	url(
        regex=r'^schools/?$', 
        view='list', 
        name='school_list'
    ),
    url(
        regex=r'^school/add/?$', 
        view='add', 
        name='school_add'
    ),
    url(
        regex=r'^school/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='school_edit'
    ),
    url(
        regex=r'^school/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='school_delete'
    ),
)