#!/usr/bin/env python
# encoding: utf-8
u"""
seized_material.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import SeizedMaterialForm
from core.models import SeizedMaterial

@login_required
def list(request):
    paginator = Paginator(SeizedMaterial.objects.all(), 10)
    try:
        seized_materials = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('seized_material_list')
    
    template_context = {
        'seized_materials': seized_materials,
    }
    return render(
        request=request,
        template_name='seized_material/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    seized_material_form = SeizedMaterialForm(
        data=request.POST or None
    )
    if seized_material_form.is_valid():
        seized_material_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('seized_material_list')
    
    template_context = {
        'seized_material_form': seized_material_form,
    }
    return render(
        request=request,
        template_name='seized_material/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, seized_material_pk):
    seized_material = get_object_or_404(
        klass=SeizedMaterial, 
        pk=seized_material_pk
    )
    seized_material_form = SeizedMaterialForm(
        data=request.POST or None,
        instance=seized_material
    )
    if seized_material_form.is_valid():
        seized_material_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('seized_material_list')

    template_context = {
        'seized_material': seized_material,
        'seized_material_form': seized_material_form,
    }
    return render(
        request=request,
        template_name='seized_material/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, seized_material_pk):
    seized_material = get_object_or_404(
        klass=SeizedMaterial, 
        pk=seized_material_pk
    )
    if request.method == 'POST':
        seized_material.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('seized_material_list')
    
    template_context = {
        'seized_material': seized_material
    }
    return render(
        request=request,
        template_name='seized_material/delete.html',
        dictionary=template_context
    )
