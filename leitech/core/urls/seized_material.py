#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 19/06/2013.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views.seized_material',
    url(
        regex=r'^seized/materials/?$', 
        view='list', 
        name='seized_material_list'
    ),
    url(
        regex=r'^seized/material/add/?$', 
        view='add', 
        name='seized_material_add'
    ),
    url(
        regex=r'^seized/material/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='seized_material_edit'
    ),
    url(
        regex=r'^seized/material/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='seized_material_delete'
    ),
)