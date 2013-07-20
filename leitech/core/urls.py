#!/usr/bin/env python
# encoding: utf-8
u"""
urls.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
    # SeizedMaterial
    url(
    	regex=r'^seized/materials/?$', 
    	view='seized_material.list', 
    	name='seized_material_list'
    ),
    url(
    	regex=r'^seized/material/add/?$', 
    	view='seized_material.add', 
    	name='seized_material_add'
    ),
    url(
    	regex=r'^seized/material/edit/(?P<pk>[a-z\d]+)?$',
    	view='seized_material.edit', 
    	name='seized_material_edit'
    ),
    url(
    	regex=r'^seized/material/delete/(?P<pk>[a-z\d]+)?$',
    	view='seized_material.delete', 
    	name='seized_material_delete'
    ),

    # SeizedMaterialType
    url(
        regex=r'^seized/material/types/?$', 
        view='seized_material_type.list', 
        name='seized_material_type_list'
    ),
    url(
        regex=r'^seized/material/type/add/?$', 
        view='seized_material_type.add', 
        name='seized_material_type_add'
    ),
    url(
        regex=r'^seized/material/type/edit/(?P<pk>[a-z\d]+)?$',
        view='seized_material_type.edit', 
        name='seized_material_type_edit'
    ),
    url(
        regex=r'^seized/material/type/delete/(?P<pk>[a-z\d]+)?$',
        view='seized_material_type.delete', 
        name='seized_material_type_delete'
    ),
)