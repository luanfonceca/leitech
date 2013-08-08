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


class HistoryModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    # Relations
    created_by = models.ForeignKey(
        to='accounts.User',
        related_name='%(app_label)s_%(class)s_created_histories',
        null=True,
        blank=True,
        editable=False,
    )
    updated_by = models.ForeignKey(
        to='accounts.User',
        related_name='%(app_label)s_%(class)s_updated_histories',
        null=True,
        blank=True,
        editable=False,
    )

    class Meta:
        abstract = True    
    

class Address(HistoryModel):
    state = models.CharField(
        max_length=3, 
        null=True, 
        blank=True, 
        choices=BR_STATE_CHOICES,
        verbose_name=_(u'UF')
    )
    city = models.CharField(
        max_length=60, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Cidade')
    )
    neighborhood = models.CharField(
        max_length=60, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Bairro')
    )
    zipcode = models.CharField(
        max_length=8, 
        null=True, 
        blank=True, 
        verbose_name=_(u'CEP')
    )
    street = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Rua')
    )
    complement = models.CharField(
        max_length=150, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Complemento')
    )
    number = models.CharField(
        max_length=10, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Número')
    )
    
    class Meta:
        db_table = 'address'
        verbose_name = _(u'Endereço')
        verbose_name_plural = _(u'Endereços')

    def __unicode__(self):
        return u'%s' % self.street


class School(HistoryModel):
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
    address = models.OneToOneField(
        to=Address,
        verbose_name=_(u'Endereço')   
    )
    
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
        to=PoliceCar, 
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


class OccurrenceStatus(HistoryModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )

    class Meta:
        db_table='occurrence_status'
        verbose_name = _(u'Status da Ocorrência')
        verbose_name_plural = _(u'Status das Ocorrências')

    def __unicode__(self):
        return u'%s' % self.name
    
    
class OccurrenceType(HistoryModel):
    name = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Nome')
    )

    class Meta:
        db_table='occurrence_type'
        verbose_name = _(u'Tipo da Ocorrência')
        verbose_name_plural = _(u'Tipos da Ocorrências')

    def __unicode__(self):
        return u'%s' % self.name


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


class Occurrence(HistoryModel):
    nature = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Natureza da Ocorrência')
    )
    relevant_information = models.CharField(
        max_length=150, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Dados Relevante')
    )
    accident_report = models.CharField(
        max_length=50, 
        null=False, 
        blank=False, 
        verbose_name=_(u'Boletim de Ocorrência')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_(u'Descrição')
    )

    # relations
    police_car = models.ForeignKey(
        to=PoliceCar, 
        null=False, 
        blank=False, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Viatura')   
    )
    school = models.ForeignKey(
        to=School, 
        null=False, 
        blank=False, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Escola')   
    )
    status = models.ForeignKey(
        to=OccurrenceStatus, 
        null=True, 
        blank=True, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Status')   
    )
    type = models.ForeignKey(
        to=OccurrenceType, 
        null=True, 
        blank=True, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Tipo')   
    )
    attended_public = models.ForeignKey(
        to=AttendedPublic, 
        null=False, 
        blank=False, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Público Atendido')   
    )
    seized_materials = models.ManyToManyField(
        to=SeizedMaterial, 
        through='core.OccurrenceSeizedMaterial',
        null=True, 
        blank=True, 
        related_name='occurrences',
        verbose_name=_(u'Materiais Apreendidos')   
    )

    class Meta:
        db_table='occurrence'
        verbose_name = _(u'Ocorrência')
        verbose_name_plural = _(u'Ocorrências')

    def __unicode__(self):
        return u'%s...' % self.description[:10]
    

class OccurrenceSeizedMaterial(HistoryModel):
    amount = models.CharField(
        max_length=150, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Quantidade ou Valor')
    )

    # relations 
    occurrence = models.ForeignKey(
        to=Occurrence,
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
