#!/usr/bin/env python
# encoding: utf-8
u"""
police_car.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.police_car',
	url(
        regex=r'^police/cars/?$', 
        view='list', 
        name='police_car_list'
    ),
    url(
        regex=r'^police/car/add/?$', 
        view='add', 
        name='police_car_add'
    ),
    url(
        regex=r'^police/car/edit/(?P<pk>[a-z\d]+)?$',
        view='edit', 
        name='police_car_edit'
    ),
    url(
        regex=r'^police/car/delete/(?P<pk>[a-z\d]+)?$',
        view='delete', 
        name='police_car_delete'
    ),
)