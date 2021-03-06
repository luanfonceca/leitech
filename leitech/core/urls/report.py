#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence.py

Criado por Luan Fonseca em 20/06/2013.
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('core.views.report',
	url(
        regex=r'^occurrences/report02/?$', 
        view='ajax_report02', 
        name='ajax_report02'
    ),

    url(
        regex=r'^occurrences/report03/?$', 
        view='ajax_report03', 
        name='ajax_report03'
    ),
    url(
        regex=r'^occurrences/report04/?$', 
        view='ajax_report04', 
        name='ajax_report04'
    ),
    url(
        regex=r'^occurrences/report05/?$', 
        view='ajax_report05', 
        name='ajax_report05'
    ),
    url(
        regex=r'^occurrences/report06/?$', 
        view='ajax_report06', 
        name='ajax_report06'
    ),
    url(
        regex=r'^occurrences/report07/?$', 
        view='ajax_report07', 
        name='ajax_report07'
    ),
    url(
        regex=r'^occurrences/report08/?$', 
        view='ajax_report08', 
        name='ajax_report08'
    ),
)