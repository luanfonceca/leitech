#!/usr/bin/env python
# encoding: utf-8
u"""
police_car.py

Criado por Luan Fonseca em 18/06/2013.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from core.forms import PoliceCarForm
from core.models import PoliceCar

@login_required
def list(request):
    paginator = Paginator(PoliceCar.objects.all(), 10)
    try:
        police_cars = paginator.page(
            request.GET.get('page', 1)
        )
    except (EmptyPage, PageNotAnInteger):
        messages.error(request, u"A página que você tentou acessar está vazia. Você foi redirecionado para a primeira página.")
        return redirect('police_car_list')
    
    template_context = {
        'police_cars': police_cars,
    }
    return render(
        request=request,
        template_name='police_car/list.html',
        dictionary=template_context
    )

@login_required
def add(request):
    police_car_form = PoliceCarForm(
        data=request.POST or None
    )
    if police_car_form.is_valid():
        police_car_form.save(auth.get_user(request))
        messages.success(request, u"Material salvo com sucesso.")
        return redirect('police_car_list')
    
    template_context = {
        'police_car_form': police_car_form,
    }
    return render(
        request=request,
        template_name='police_car/add.html',
        dictionary=template_context
    )

@login_required
def edit(request, pk):
    police_car = get_object_or_404(
        klass=PoliceCar, 
        pk=pk
    )
    police_car_form = PoliceCarForm(
        data=request.POST or None,
        instance=police_car
    )
    if police_car_form.is_valid():
        police_car_form.save(auth.get_user(request))
        messages.success(request, u"Material editado com sucesso.")
        return redirect('police_car_list')

    template_context = {
        'police_car': police_car,
        'police_car_form': police_car_form,
    }
    return render(
        request=request,
        template_name='police_car/edit.html',
        dictionary=template_context
    )

@login_required
def delete(request, pk):
    police_car = get_object_or_404(
        klass=PoliceCar, 
        pk=pk
    )
    if request.method == 'POST':
        police_car.delete()
        messages.success(request, u"Material removido com sucesso.")
        return redirect('police_car_list')
    
    template_context = {
        'police_car': police_car
    }
    return render(
        request=request,
        template_name='police_car/delete.html',
        dictionary=template_context
    )
