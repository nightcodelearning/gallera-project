# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
from django.conf import settings

from decimal import Decimal
from functools import partial
from django.db import models
from gallera.models import ManagedTVModel
from gallera.utils import generate_token
from uuid import uuid4
from django.db import models, transaction


from django.utils.translation import get_language, activate
activate('es')

def get_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join('photos', filename)


class Search(ManagedTVModel):
    token = models.CharField(
        unique=True,
        max_length=255,
        help_text='unique identifier for search from this system',
        default=partial(generate_token, 's'),
    )

    group_date = models.CharField(max_length=255, blank=True)

    count = models.IntegerField(default=0)

    def __str__(self):
        return self.group_date


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
        return self.full_name


class Chick(ManagedTVModel):
    """
    Describes a Chick stored in the application.
    """
    COLOR_CHINO = 'CHINO'
    COLOR_MORADO = 'MORADO'
    COLOR_JABADO = 'JABADO'
    COLOR_RED = 'PINTO'
    COLOR_OTHER = 'OTRO'

    ALLOWED_COLORS = [
        ('CHINO', COLOR_CHINO),
        ('MORADO', COLOR_MORADO),
        ('JABADO', COLOR_JABADO),
        ('PINTO', COLOR_RED),
        ('OTRO', COLOR_OTHER),
    ]

    CRESTA_PALMA = 'PALMA'
    CRESTA_ROSA = 'ROSA'
    CRESTA_OTRA = 'OTRA'

    ALLOWED_CRESTA = [
        ('PALMA', CRESTA_PALMA),
        ('ROSA', CRESTA_ROSA),
        ('OTRA', CRESTA_OTRA)
    ]

    PATA_BLANCA = 'PATIBLANCO'
    PATA_AMARILLA = 'PATIAMARILLO'
    PATA_OTRA = 'OTRO'

    ALLOWED_PATA = [
        ('PATIBLANCO', PATA_BLANCA),
        ('PATIAMARILLO', PATA_AMARILLA),
        ('OTRO', PATA_OTRA)
    ]

    token = models.CharField(
        unique=True,
        max_length=255,
        help_text='unique identifier for chick from this system',
        default=partial(generate_token, 'c'),
        editable=False
    )

    image = models.ImageField(
        db_column='image',
        upload_to=get_image_path,
        default='',
    )

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    owner = models.ForeignKey(
        Owner, models.DO_NOTHING, blank=True, null=True,
    )

    search_group = models.ForeignKey(
        Search, models.DO_NOTHING, blank=True, null=True,
    )

    # search_group = models.OneToOneField(Search, related_name="course_taken")

    @property
    def owner_name(self):
        return self.owner.full_name

    breeder_plate_number = models.CharField(max_length=255, blank=True)
    breeder_name = models.CharField(max_length=255, blank=True)

    # register_date2 = models.DateTimeField(auto_now=True)

    @property
    def register_date(self):
        import locale
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        return self.date_created.strftime('%B - %Y')

    coliseo_plate_number = models.CharField(max_length=255, blank=True)
    coliseo_responsible = models.CharField(max_length=255, blank=True)

    weight = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        default=Decimal(0),
    )

    color = models.CharField(
        max_length=20,
        choices=ALLOWED_COLORS,
        default=COLOR_CHINO,
    )
    cresta = models.CharField(
        max_length=20,
        choices=ALLOWED_CRESTA,
        default=CRESTA_PALMA,
    )
    pata = models.CharField(
        max_length=20,
        choices=ALLOWED_PATA,
        default=PATA_BLANCA,
    )

    def __str__(self):
        return self.coliseo_plate_number

    @transaction.atomic
    def save(self, *args, **kwargs):
        models.DateTimeField(auto_now=True)
        import datetime
        date = datetime.datetime.now()
        self.search_group, _ = Search.objects.get_or_create(
            group_date=date.strftime('%B - %Y'))
        self.search_group.count = self.search_group.count+1
        self.search_group.save()
        super(Chick, self).save(*args, **kwargs)


