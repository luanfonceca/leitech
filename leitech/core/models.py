#!/usr/bin/env python
# encoding: utf-8
u"""
models.py

Criado por Luan Fonseca em 17/06/2013.
"""

from django.db import models
from django.utils.translation import ugettext as _
from django_localflavor_br.br_states import STATE_CHOICES as BR_STATE_CHOICES
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)

from utils import now, send_mail


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        _now = now()
        if not email:
            raise ValueError('The given email must be set.')
        email = UserManager.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=True,
            is_active=True,
            is_superuser=False,
            last_login=_now,
            date_joined=_now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email,
            password,
            **extra_fields
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=50
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=50,
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        db_index=True
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    is_manager = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )

    # Django Managers
    objects = UserManager()

    # Configs
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        verbose_name = _(u'Profile')
        verbose_name_plural = _(u'Profiles')

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])


class Address(models.Model):
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
        verbose_name = _(u'Address')
        verbose_name_plural = _(u'Addresses')

    def __unicode__(self):
        return u'%s' % self.street


class School(models.Model):
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
    address = models.OneToOneField(
        to=Address,
        verbose_name=_(u'Endereço')   
    )
    
    class Meta:
        db_table = 'school'
        verbose_name = _(u'School')
        verbose_name_plural = _(u'Schools')

    def __unicode__(self):
        return u'%s' % self.name