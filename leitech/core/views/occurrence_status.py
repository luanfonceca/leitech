#!/usr/bin/env python
# encoding: utf-8
u"""
occurrence_status.py

Criado por Luan Fonseca em 17/08/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import OccurrenceStatusForm
from core.models import OccurrenceStatus

@login_required
def list(request):
    paginator = Paginator(OccurrenceStatus.objects.all(), 10)
    try:
        occurrence_status = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('occurrence_status_list')
    
    template_context = {
        'occurrence_status': occurrence_status,
    }
    return render(
        request=request,
        template_name='occurrence_status/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    occurrence_status_form = OccurrenceStatusForm(
        data=request.POST or None
    )
    if occurrence_status_form.is_valid():
        occurrence_status_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('occurrence_status_list')
    
    template_context = {
        'occurrence_status_form': occurrence_status_form,
    }
    return render(
        request=request,
        template_name='occurrence_status/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    occurrence_status = get_object_or_404(
        klass=OccurrenceStatus, 
        pk=pk
    )
    occurrence_status_form = OccurrenceStatusForm(
        data=request.POST or None,
        instance=occurrence_status
    )
    if occurrence_status_form.is_valid():
        occurrence_status_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('occurrence_status_list')

    template_context = {
        'occurrence_status': occurrence_status,
        'occurrence_status_form': occurrence_status_form,
    }
    return render(
        request=request,
        template_name='occurrence_status/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    occurrence_status = get_object_or_404(
        klass=OccurrenceStatus, 
        pk=pk
    )
    if request.method == 'POST':
        occurrence_status.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('occurrence_status_list')
    
    template_context = {
        'occurrence_status': occurrence_status
    }
    return render(
        request=request,
        template_name='occurrence_status/delete.html',
        dictionary=template_context
    )
