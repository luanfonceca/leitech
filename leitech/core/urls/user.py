#!/usr/bin/env python
# encoding: utf-8
u"""
user.py

Criado por Luan Fonseca em 29/07/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.user',
	url(
        regex=r'^users/?$', 
        view='list', 
        name='user_list'
    ),
    url(
        regex=r'^user/add/?$', 
        view='add', 
        name='user_add'
    ),
    url(
        regex=r'^user/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='user_edit'
    ),
    url(
        regex=r'^user/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='user_delete'
    ),
)