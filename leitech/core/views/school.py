#!/usr/bin/env python
# encoding: utf-8
u"""
school.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import SchoolForm
from core.models import School

@login_required
def list(request):
    paginator = Paginator(School.objects.all(), 10)
    try:
        schools = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('school_list')
    
    template_context = {
        'schools': schools,
    }
    return render(
        request=request,
        template_name='school/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    school_form = SchoolForm(
        data=request.POST or None
    )
    if school_form.is_valid():
        school_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('school_list')
    
    template_context = {
        'school_form': school_form,
    }
    return render(
        request=request,
        template_name='school/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    school = get_object_or_404(
        klass=School, 
        pk=pk
    )
    school_form = SchoolForm(
        data=request.POST or None,
        instance=school
    )
    if school_form.is_valid():
        school_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('school_list')

    template_context = {
        'school': school,
        'school_form': school_form,
    }
    return render(
        request=request,
        template_name='school/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    school = get_object_or_404(
        klass=School, 
        pk=pk
    )
    if request.method == 'POST':
        school.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('school_list')
    
    template_context = {
        'school': school
    }
    return render(
        request=request,
        template_name='school/delete.html',
        dictionary=template_context
    )
