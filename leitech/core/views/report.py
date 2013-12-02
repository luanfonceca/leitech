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
