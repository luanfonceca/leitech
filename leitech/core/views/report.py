#!/usr/bin/env python
# encoding: utf-8

from django.db.models.aggregates import Count

from core.models import Occurrence
from leitech.utils import JsonHttpResponse

def ajax_report02(request):
    data = Occurrence.objects.values_list('attended_public__name')\
                             .annotate(Count('attended_public'))
    return JsonHttpResponse(list(data))
