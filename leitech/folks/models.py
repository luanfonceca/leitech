#!/usr/bin/env python
# encoding: utf-8
u"""
models.py

Criado por Luan Fonseca em 17/06/2013.
"""

from django.db import models
from django.utils.translation import ugettext as _
from django_localflavor_br.br_states import STATE_CHOICES as BR_STATE_CHOICES

from utils import now, send_mail
from core.models import HistoryModel, AddressedModel



class School(HistoryModel, AddressedModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )
    phone = models.CharField(
        max_length=150, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Telefone')
    )

    # Relations
    # address = models.OneToOneField(
    #     to='folks.Address',
    #     verbose_name=_(u'Endereço')   
    # )
    
    class Meta:
        db_table = 'school'
        verbose_name = _(u'Escola')
        verbose_name_plural = _(u'Escolas')

    def __unicode__(self):
        return u'%s' % self.name


class PoliceCar(HistoryModel):
    ident = models.CharField(
        max_length=50, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Identificador')
    )

    class Meta:
        db_table='police_car'
        verbose_name = _(u'Viatura')
        verbose_name_plural = _(u'Viaturas')

    def __unicode__(self):
        return u'%s' % self.ident
    

class Police(HistoryModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )

    # Relations
    police_car = models.ForeignKey(
        to='folks.PoliceCar', 
        null=True, 
        blank=True, 
        related_name='polices', 
        on_delete=models.CASCADE,
        verbose_name=_(u'Viatura')   
    )
    
    class Meta:
        db_table='police'
        verbose_name = _(u'Policial')
        verbose_name_plural = _(u'Policiais')

    def __unicode__(self):
        return u'%s' % self.name


class AttendedPublic(HistoryModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )

    class Meta:
        db_table='attended_public'
        verbose_name = _(u'Público Atendido')
        verbose_name_plural = _(u'Público Atendido')

    def __unicode__(self):
        return u'%s' % self.name