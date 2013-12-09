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


class AddressedModel(models.Model):
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
        verbose_name=_(u'Bairro'),
        choices=[
            ('alecrim', 'Alecrim'),
            ('areia preta', 'Areia Preta'),
            ('bairro nordeste', 'Bairro Nordeste'),
            ('barro vermelho', 'Barro Vermelho'),
            ('bom pastor', 'Bom Pastor'),
            ('candelária', 'Candelária'),
            ('capim macio', 'Capim Macio'),
            ('cidade alta', 'Cidade Alta'),
            ('cidade da esperança', 'Cidade da Esperança'),
            ('cidade nova', 'Cidade Nova'),
            ('dix-sept rosado', 'Dix-Sept Rosado'),
            ('felipe camarão', 'Felipe Camarão'),
            ('guarapes', 'Guarapes'),
            ('igapó', 'Igapó'),
            ('lagoa azul', 'Lagoa Azul'),
            ('lagoa nova', 'Lagoa Nova'),
            ('lagoa seca', 'Lagoa Seca'),
            ('mãe luíza', 'Mãe Luíza'),
            ('mirassol', 'Mirassol'),
            ('neópolis', 'Neópolis'),
            ('nossa senhora da apresentação', 'Nossa Senhora da Apresentação'),
            ('nossa senhora de nazaré', 'Nossa Senhora de Nazaré'),
            ('nova descoberta', 'Nova Descoberta'),
            ('pajuçara', 'Pajuçara'),
            ('petrópolis', 'Petrópolis'),
            ('pirangi', 'Pirangi'),
            ('pitimbu', 'Pitimbu'),
            ('planalto', 'Planalto'),
            ('ponta negra', 'Ponta Negra'),
            ('potengi', 'Potengi'),
            ('praia do meio', 'Praia do Meio'),
            ('quintas', 'Quintas'),
            ('redinha', 'Redinha'),
            ('ribeira', 'Ribeira'),
            ('rocas', 'Rocas'),
            ('salinas', 'Salinas'),
            ('santos reis', 'Santos Reis'),
            ('satélite', 'Satélite'),
            ('tirol', 'Tirol'),
        ]
    )
    zipcode = models.CharField(
        max_length=8, 
        null=True, 
        blank=True, 
        verbose_name=_(u'CEP')
    )
    street = models.CharField(
        max_length=150, 
        null=True, 
        blank=True, 
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
    region = models.CharField(
        max_length=10, 
        null=True, 
        blank=True, 
        verbose_name=_(u'Região'),
        choices=[
            ('norte', 'Norte'),
            ('sul', 'Sul'),
            ('leste', 'Leste'),
            ('oeste', 'Oeste'),
        ],
    )

    class Meta:
        abstract = True
    #     db_table = 'address'
    #     verbose_name = _(u'Endereço')
    #     verbose_name_plural = _(u'Endereços')

    # def __unicode__(self):
    #     return u'%s' % self.street


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


class Occurrence(HistoryModel, AddressedModel):
    """
    Model para a tabela de Ocorrência, que visa por
    gerenciar as Ocorrências atendidas pelo RONDA.

    @cvar nature: Natureza da Ocorrência.
    @type nature: Texto
    """
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
        null=True, 
        blank=True, 
        verbose_name=_(u'Boletim de Ocorrência')
    )
    description = models.TextField(
        blank=True,
        verbose_name=_(u'Descrição')
    )

    # relations
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
    police_car = models.ForeignKey(
        to='folks.PoliceCar', 
        null=False, 
        blank=False, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Viatura')   
    )
    school = models.ForeignKey(
        to='folks.School', 
        null=True, 
        blank=True, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Escola')   
    )
    # address = models.ForeignKey(
    #     to='folks.Address', 
    #     null=True, 
    #     blank=True, 
    #     related_name='occurrences', 
    #     on_delete=models.PROTECT,
    #     verbose_name=_(u'Endereço')
    # )
    attended_public = models.ForeignKey(
        to='folks.AttendedPublic', 
        null=False, 
        blank=False, 
        related_name='occurrences', 
        on_delete=models.PROTECT,
        verbose_name=_(u'Público Atendido')   
    )
    seized_materials = models.ManyToManyField(
        to='materials.SeizedMaterial',
        through='materials.OccurrenceSeizedMaterial',
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
