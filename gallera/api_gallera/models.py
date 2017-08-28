# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal
from functools import partial
from django.db import models
from gallera.models import ManagedTVModel
from gallera.utils import generate_token


class Chick(ManagedTVModel):
    """
    Describes a Chick stored in the application.
    """

    ALLOWED_COLORS = [('ROJO', 'ROJO'), ('OTRO', 'OTRO'), ('', '')]

    COLOR_RED = 'ROJO'
    COLOR_OTHER = 'OTRO'

    token = models.CharField(
        unique=True,
        max_length=255,
        help_text='unique identifier for chick from this system',
        default=partial(generate_token, 'c'),
    )
    owner = models.ForeignKey('api_gallera.Owner')

    born_date = models.DateTimeField(auto_now=True)

    castador_tag = models.CharField(max_length=255, blank=True)
    castador_name = models.CharField(max_length=255, blank=True)

    coliseo_tag = models.CharField(max_length=255, blank=True)
    tagger_name = models.CharField(max_length=255, blank=True)

    weight = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        default=Decimal(0),
    )

    color = models.CharField(
        max_length=4, choices=ALLOWED_COLORS, blank=True, default=''
    )


    def __str__(self):
        return self.castador_tag


class Owner(ManagedTVModel):
    """
    Describes an Chick's Owner
    """

    ALLOWED_ID_TYPES = [('CC', 'CC'), ('CE', 'CE'), ('NIT', 'NIT'),
                        ('TI', 'TI'), ('PA', 'PA'), ('', '')]

    ID_TYPE_CC = 'CC'
    ID_TYPE_CE = 'CE'
    ID_TYPE_NIT = 'NIT'
    ID_TYPE_TI = 'TI'
    ID_TYPE_PA = 'PA'

    token = models.CharField(
        unique=True,
        max_length=255,
        help_text='unique identifier for owner from this system',
        default=partial(generate_token, 'ow'),
    )
    legal_id_type = models.CharField(
        max_length=4, choices=ALLOWED_ID_TYPES, blank=True, default=''
    )
    legal_id_number = models.CharField(max_length=20, blank=True, default='')
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['legal_id_number']),
        ]

    def __str__(self):
        return self.legal_id_number


