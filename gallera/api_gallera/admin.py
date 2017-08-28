# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Owner
from .models import Chick

admin.site.register(Owner)
admin.site.register(Chick)

