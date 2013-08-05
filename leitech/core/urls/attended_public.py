#!/usr/bin/env python
# encoding: utf-8
u"""
attended_public.py

Criado por Luan Fonseca em 05/08/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.attended_public',
	url(
        regex=r'^attended/publics/?$', 
        view='list', 
        name='attended_public_list'
    ),
    url(
        regex=r'^attended/public/add/?$', 
        view='add', 
        name='attended_public_add'
    ),
    url(
        regex=r'^attended/public/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='attended_public_edit'
    ),
    url(
        regex=r'^attended/public/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='attended_public_delete'
    ),
)