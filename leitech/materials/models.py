#!/usr/bin/env python
# encoding: utf-8
u"""
models.py

Criado por Luan Fonseca em 08/08/2013.
"""
from django.db import models
from django.utils.translation import ugettext as _

from core.models import HistoryModel

class SeizedMaterialType(HistoryModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )

    class Meta:
        db_table='seized_material_type'
        verbose_name = _(u'Tipo do Material')
        verbose_name_plural = _(u'Tipos dos Materias')

    def __unicode__(self):
        return u'%s' % self.name


class SeizedMaterial(HistoryModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )

    # relations
    type = models.ForeignKey(
        to=SeizedMaterialType, 
        null=True, 
        blank=True, 
        related_name='seized_materials', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Tipo do Material')   
    )

    class Meta:
        db_table='seized_material'
        verbose_name = _(u'Material Apreendido')
        verbose_name_plural = _(u'Materiais Apreendidos')

    def __unicode__(self):
        return u'%s' % self.name


class OccurrenceSeizedMaterial(HistoryModel):
    amount = models.CharField(
        max_length=150, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Quantidade ou Valor')
    )

    # relations 
    occurrence = models.ForeignKey(
        to='core.Occurrence',
        related_name='occurrence_seized_material', 
        verbose_name=u'Ocorrência',
    )
    seized_material = models.ForeignKey(
        to=SeizedMaterial,
        related_name='occurrence_seized_material', 
        verbose_name=u'Material Apreendido',
    )
    
    class Meta:
        db_table='occurrence_seized_material'
        verbose_name = _(u'Material Apreendido na Ocorrência')
        verbose_name_plural = _(u'Materiais Apreendidos na Ocorrência')

    def __unicode__(self):
        return u'%s' % self.seized_material.name
