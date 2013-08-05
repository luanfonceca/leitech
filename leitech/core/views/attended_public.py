#!/usr/bin/env python
# encoding: utf-8
u"""
attended_public.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import AttendedPublicForm
from core.models import AttendedPublic

@login_required
def list(request):
    paginator = Paginator(AttendedPublic.objects.all(), 10)
    try:
        attended_publics = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('attended_public_list')
    
    template_context = {
        'attended_publics': attended_publics,
    }
    return render(
        request=request,
        template_name='attended_public/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    attended_public_form = AttendedPublicForm(
        data=request.POST or None
    )
    if attended_public_form.is_valid():
        attended_public_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('attended_public_list')
    
    template_context = {
        'attended_public_form': attended_public_form,
    }
    return render(
        request=request,
        template_name='attended_public/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    attended_public = get_object_or_404(
        klass=AttendedPublic, 
        pk=pk
    )
    attended_public_form = AttendedPublicForm(
        data=request.POST or None,
        instance=attended_public
    )
    if attended_public_form.is_valid():
        attended_public_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('attended_public_list')

    template_context = {
        'attended_public': attended_public,
        'attended_public_form': attended_public_form,
    }
    return render(
        request=request,
        template_name='attended_public/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    attended_public = get_object_or_404(
        klass=AttendedPublic, 
        pk=pk
    )
    if request.method == 'POST':
        attended_public.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('attended_public_list')
    
    template_context = {
        'attended_public': attended_public
    }
    return render(
        request=request,
        template_name='attended_public/delete.html',
        dictionary=template_context
    )
