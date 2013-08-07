#!/usr/bin/env python
# encoding: utf-8
u"""
address.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.address',
	url(
        regex=r'^addresses/?$', 
        view='list', 
        name='addresses_list'
    ),
    url(
        regex=r'^address/add/?$', 
        view='add', 
        name='address_add'
    ),
    url(
        regex=r'^address/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='address_edit'
    ),
    url(
        regex=r'^address/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='address_delete'
    ),
)