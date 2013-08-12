#!/usr/bin/env python
# encoding: utf-8
u"""
police.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from folks.forms import PoliceForm
from folks.models import Police

@login_required
def list(request):
    paginator = Paginator(Police.objects.all(), 10)
    try:
        polices = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('police_list')
    
    template_context = {
        'polices': polices,
    }
    return render(
        request=request,
        template_name='police/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    police_form = PoliceForm(
        data=request.POST or None
    )
    if police_form.is_valid():
        police_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('police_list')
    
    template_context = {
        'police_form': police_form,
    }
    return render(
        request=request,
        template_name='police/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    police = get_object_or_404(
        klass=Police, 
        pk=pk
    )
    police_form = PoliceForm(
        data=request.POST or None,
        instance=police
    )
    if police_form.is_valid():
        police_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('police_list')

    template_context = {
        'police': police,
        'police_form': police_form,
    }
    return render(
        request=request,
        template_name='police/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    police = get_object_or_404(
        klass=Police, 
        pk=pk
    )
    if request.method == 'POST':
        police.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('police_list')
    
    template_context = {
        'police': police
    }
    return render(
        request=request,
        template_name='police/delete.html',
        dictionary=template_context
    )
