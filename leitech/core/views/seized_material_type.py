#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material_type.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import SeizedMaterialTypeForm
from core.models import SeizedMaterialType

@login_required
def list(request):
    paginator = Paginator(SeizedMaterialType.objects.all(), 10)
    try:
        seized_material_types = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('seized_material_type_list')
    
    template_context = {
        'seized_material_types': seized_material_types,
    }
    return render(
        request=request,
        template_name='seized_material_type/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    seized_material_type_form = SeizedMaterialTypeForm(
        data=request.POST or None
    )
    if seized_material_type_form.is_valid():
        seized_material_type_form.save(auth.get_user(request))
        messages.success(request, u"Tipo de Material salvo com sucesso.")
        return redirect('seized_material_type_list')
    
    template_context = {
        'seized_material_type_form': seized_material_type_form,
    }
    return render(
        request=request,
        template_name='seized_material_type/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    seized_material_type = get_object_or_404(
        klass=SeizedMaterialType, 
        pk=pk
    )
    seized_material_type_form = SeizedMaterialTypeForm(
        data=request.POST or None,
        instance=seized_material_type
    )
    if seized_material_type_form.is_valid():
        seized_material_type_form.save(auth.get_user(request))
        messages.success(request, u"Tipo de Material editado com sucesso.")
        return redirect('seized_material_type_list')

    template_context = {
        'seized_material_type': seized_material_type,
        'seized_material_type_form': seized_material_type_form,
    }
    return render(
        request=request,
        template_name='seized_material_type/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    seized_material_type = get_object_or_404(
        klass=SeizedMaterialType, 
        pk=pk
    )
    if request.method == 'POST':
        seized_material_type.delete()
        messages.success(request, u"Tipo de Material removido com sucesso.")
        return redirect('seized_material_type_list')
    
    template_context = {
        'seized_material_type': seized_material_type
    }
    return render(
        request=request,
        template_name='seized_material_type/delete.html',
        dictionary=template_context
    )
