#!/usr/bin/env python
# encoding: utf-8
u"""
user.py

Criado por Luan Fonseca em 08/08/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from accounts.forms import UserForm, UserEditForm
from accounts.models import User

@login_required
def list(request):
    paginator = Paginator(User.objects.all(), 10)
    try:
        users = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('user_list')
    
    template_context = {
        'users': users,
    }
    return render(
        request=request,
        template_name='list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    user_form = UserForm(
        data=request.POST or None
    )
    if user_form.is_valid():
        user_form.save(auth.get_user(request))
        messages.success(request, u"Usuário salvo com sucesso.")
        return redirect('user_list')
    
    template_context = {
        'user_form': user_form,
    }
    return render(
        request=request,
        template_name='add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    user = get_object_or_404(
        klass=User, 
        pk=pk
    )
    user_form = UserEditForm(
        data=request.POST or None,
        instance=user
    )
    if user_form.is_valid():
        user_form.save(auth.get_user(request))
        messages.success(request, u"Usuário editado com sucesso.")
        return redirect('user_list')

    template_context = {
        'user': user,
        'user_form': user_form,
    }
    return render(
        request=request,
        template_name='edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    user = get_object_or_404(
        klass=User, 
        pk=pk
    )
    if request.method == 'POST':
        user.delete()
        messages.success(request, u"Usuário removido com sucesso.")
        return redirect('user_list')
    
    template_context = {
        'user': user
    }
    return render(
        request=request,
        template_name='delete.html',
        dictionary=template_context
    )
