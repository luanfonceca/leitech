#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material_type.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.seized_material_type',
	url(
        regex=r'^seized/material/types/?$', 
        view='list', 
        name='seized_material_type_list'
    ),
    url(
        regex=r'^seized/material/type/add/?$', 
        view='add', 
        name='seized_material_type_add'
    ),
    url(
        regex=r'^seized/material/type/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='seized_material_type_edit'
    ),
    url(
        regex=r'^seized/material/type/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='seized_material_type_delete'
    ),
)