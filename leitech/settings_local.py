#!/usr/bin/env python
# encoding: utf-8
u"""
settings_local.py
Criado por Luan Fonseca em 12/06/2013.

Arquivo de Configurações locais, cada usuários deste código deverá colocar suas
configurações do projeto aqui, e nunca versionar suas informações, apenas novas
configurações quando houver.
"""

from settings import *

ADMINS += (
    # ('Your Name', 'your_email@example.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
