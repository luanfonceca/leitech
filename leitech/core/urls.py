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
    	regex=r'^seized_materials/?$', 
    	view='seized_material.list', 
    	name='seized_material_list'
    ),
    url(
    	regex=r'^seized_material/add/?$', 
    	view='seized_material.add', 
    	name='seized_material_add'
    ),
    url(
    	regex=r'^seized_material/edit/(?P<seized_material_pk>[a-z\d]+)?$',
    	view='seized_material.edit', 
    	name='seized_material_edit'
    ),
    url(
    	regex=r'^seized_material/delete/(?P<seized_material_pk>[a-z\d]+)?$',
    	view='seized_material.delete', 
    	name='seized_material_delete'
    ),
)