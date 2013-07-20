#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence_type.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import OccurrenceTypeForm
from core.models import OccurrenceType

@login_required
def list(request):
    paginator = Paginator(OccurrenceType.objects.all(), 10)
    try:
        occurrence_types = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('occurrence_type_list')
    
    template_context = {
        'occurrence_types': occurrence_types,
    }
    return render(
        request=request,
        template_name='occurrence_type/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    occurrence_type_form = OccurrenceTypeForm(
        data=request.POST or None
    )
    if occurrence_type_form.is_valid():
        occurrence_type_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('occurrence_type_list')
    
    template_context = {
        'occurrence_type_form': occurrence_type_form,
    }
    return render(
        request=request,
        template_name='occurrence_type/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    occurrence_type = get_object_or_404(
        klass=OccurrenceType, 
        pk=pk
    )
    occurrence_type_form = OccurrenceTypeForm(
        data=request.POST or None,
        instance=occurrence_type
    )
    if occurrence_type_form.is_valid():
        occurrence_type_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('occurrence_type_list')

    template_context = {
        'occurrence_type': occurrence_type,
        'occurrence_type_form': occurrence_type_form,
    }
    return render(
        request=request,
        template_name='occurrence_type/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    occurrence_type = get_object_or_404(
        klass=OccurrenceType, 
        pk=pk
    )
    if request.method == 'POST':
        occurrence_type.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('occurrence_type_list')
    
    template_context = {
        'occurrence_type': occurrence_type
    }
    return render(
        request=request,
        template_name='occurrence_type/delete.html',
        dictionary=template_context
    )
