#!/usr/bin/env python
# encoding: utf-8
u"""
police.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views.police',
	url(
        regex=r'^polices/?$', 
        view='list', 
        name='police_list'
    ),
    url(
        regex=r'^police/add/?$', 
        view='add', 
        name='police_add'
    ),
    url(
        regex=r'^police/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='police_edit'
    ),
    url(
        regex=r'^police/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='police_delete'
    ),
)