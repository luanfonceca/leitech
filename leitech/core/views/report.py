#!/usr/bin/env python
# encoding: utf-8

from django.db.models.aggregates import Count
from django.http import HttpResponse
from simplejson import dumps as json_dumps

from core.models import Occurrence


def JsonHttpResponse(data, **kw):
	return HttpResponse(json_dumps(data, encoding='utf-8', **kw))

def ajax_report02(request):
    data = Occurrence.objects.values_list('attended_public__name')\
                             .annotate(Count('attended_public'))
    return JsonHttpResponse(list(data))

def ajax_report03(request):
    data = Occurrence.objects.filter(address__region__isnull=False)\
                             .values_list('address__region')\
                             .annotate(Count('address__region'))
    return JsonHttpResponse(list(data))    

def ajax_report04(request):
    data = Occurrence.objects.filter(address__region__isnull=False)\
                             .values_list('address__neighborhood')\
                             .annotate(Count('address__neighborhood'))
    return JsonHttpResponse(list(data))    

def ajax_report05(request):
    data = Occurrence.objects.filter(type__isnull=False)\
                             .values_list('type__name')\
                             .annotate(Count('type'))
    return JsonHttpResponse(list(data))    

def ajax_report06(request):
    # data = Occurrence.objects.filter(created_by__isnull=False)\
    #                          .values_list('created_at')\
    #                          .annotate(Count('id'))
    data = []
    weekdays = {
        0: u'Domingo', 
        1: u'Segunda', 
        2: u'Terça', 
        3: u'Quarta', 
        4: u'Quinta',  
        5: u'Sexta', 
        6: u'Sábado'
    }
    for day in weekdays.keys():
        data.append(
            (weekdays[day],
            Occurrence.objects.filter(
                created_at__week_day=day
            ).count())
        )
        
    return JsonHttpResponse(data)    
