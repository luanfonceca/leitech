#!/usr/bin/env python
# encoding: utf-8
u"""
address.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from folks.forms import AddressForm
from folks.models import Address

@login_required
def list(request):
    paginator = Paginator(Address.objects.all(), 10)
    try:
        addresses = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('addresses_list')
    
    template_context = {
        'addresses': addresses,
    }
    return render(
        request=request,
        template_name='address/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    address_form = AddressForm(
        data=request.POST or None
    )
    if address_form.is_valid():
        address_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('addresses_list')
    
    template_context = {
        'address_form': address_form,
    }
    return render(
        request=request,
        template_name='address/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    address = get_object_or_404(
        klass=Address, 
        pk=pk
    )
    address_form = AddressForm(
        data=request.POST or None,
        instance=address
    )
    if address_form.is_valid():
        address_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('addresses_list')

    template_context = {
        'address': address,
        'address_form': address_form,
    }
    return render(
        request=request,
        template_name='address/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    address = get_object_or_404(
        klass=Address, 
        pk=pk
    )
    if request.method == 'POST':
        address.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('addresses_list')
    
    template_context = {
        'address': address
    }
    return render(
        request=request,
        template_name='address/delete.html',
        dictionary=template_context
    )
