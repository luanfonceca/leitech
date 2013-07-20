#!/usr/bin/env python
# encoding: utf-8
u"""
urls.py

Criado por Luan Fonseca em 19/06/2013.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('core.views',
	# OccurrenceType
    url(
        regex=r'^occurrence/types/?$', 
        view='occurrence_type.list', 
        name='occurrence_type_list'
    ),
    url(
        regex=r'^occurrence/type/add/?$', 
        view='occurrence_type.add', 
        name='occurrence_type_add'
    ),
    url(
        regex=r'^occurrence/type/edit/(?P<pk>[a-z\d]+)?$',
        view='occurrence_type.edit', 
        name='occurrence_type_edit'
    ),
    url(
        regex=r'^occurrence/type/delete/(?P<pk>[a-z\d]+)?$',
        view='occurrence_type.delete', 
        name='occurrence_type_delete'
    ),

    # Police
    url(
        regex=r'^polices/?$', 
        view='police.list', 
        name='police_list'
    ),
    url(
        regex=r'^police/add/?$', 
        view='police.add', 
        name='police_add'
    ),
    url(
        regex=r'^police/edit/(?P<pk>[a-z\d]+)?$',
        view='police.edit', 
        name='police_edit'
    ),
    url(
        regex=r'^police/delete/(?P<pk>[a-z\d]+)?$',
        view='police.delete', 
        name='police_delete'
    ),

    # PoliceCar
    url(
        regex=r'^police/cars/?$', 
        view='police_car.list', 
        name='police_car_list'
    ),
    url(
        regex=r'^police/car/add/?$', 
        view='police_car.add', 
        name='police_car_add'
    ),
    url(
        regex=r'^police/car/edit/(?P<pk>[a-z\d]+)?$',
        view='police_car.edit', 
        name='police_car_edit'
    ),
    url(
        regex=r'^police/car/delete/(?P<pk>[a-z\d]+)?$',
        view='police_car.delete', 
        name='police_car_delete'
    ),

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

    # School
    url(
        regex=r'^schools/?$', 
        view='school.list', 
        name='school_list'
    ),
    url(
        regex=r'^school/add/?$', 
        view='school.add', 
        name='school_add'
    ),
    url(
        regex=r'^school/edit/(?P<pk>[a-z\d]+)?$',
        view='school.edit', 
        name='school_edit'
    ),
    url(
        regex=r'^school/delete/(?P<pk>[a-z\d]+)?$',
        view='school.delete', 
        name='school_delete'
    ),

    # Occurrence
    url(
        regex=r'^occurrences/?$', 
        view='occurrence.list', 
        name='occurrence_list'
    ),
    url(
        regex=r'^occurrence/add/?$', 
        view='occurrence.add', 
        name='occurrence_add'
    ),
    url(
        regex=r'^occurrence/edit/(?P<pk>[a-z\d]+)?$',
        view='occurrence.edit', 
        name='occurrence_edit'
    ),
    url(
        regex=r'^occurrence/delete/(?P<pk>[a-z\d]+)?$',
        view='occurrence.delete', 
        name='occurrence_delete'
    ),
)