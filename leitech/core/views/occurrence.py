#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from materials.forms import OSMFormSet
from core.forms import OccurrenceForm
from core.models import Occurrence

@login_required
def list(request):
    paginator = Paginator(Occurrence.objects.all(), 10)
    try:
        occurrences = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('occurrence_list')
    
    template_context = {
        'occurrences': occurrences,
    }
    return render(
        request=request,
        template_name='occurrence/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    osm_formset = OSMFormSet(
        data=request.POST or None, 
        instance=Occurrence()
    )
    occurrence_form = OccurrenceForm(
        data=request.POST or None
    )
    if occurrence_form.is_valid() and osm_formset.is_valid():
        occurrence = occurrence_form.save(auth.get_user(request))
        osm_formset.instance = occurrence
        osm_formset.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('occurrence_list')
    
    template_context = {
        'occurrence_form': occurrence_form,
        'osm_formset': osm_formset,
    }
    return render(
        request=request,
        template_name='occurrence/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    occurrence = get_object_or_404(
        klass=Occurrence, 
        pk=pk
    )
    osm_formset = OSMFormSet(
        data=request.POST or None, 
        instance=occurrence
    )
    occurrence_form = OccurrenceForm(
        data=request.POST or None,
        instance=occurrence
    )
    if occurrence_form.is_valid():
        occurrence_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('occurrence_list')

    template_context = {
        'occurrence': occurrence,
        'occurrence_form': occurrence_form,
        'osm_formset': osm_formset,
    }
    return render(
        request=request,
        template_name='occurrence/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    occurrence = get_object_or_404(
        klass=Occurrence, 
        pk=pk
    )
    if request.method == 'POST':
        occurrence.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('occurrence_list')
    
    template_context = {
        'occurrence': occurrence
    }
    return render(
        request=request,
        template_name='occurrence/delete.html',
        dictionary=template_context
    )
