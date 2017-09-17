#-*- coding: utf-8 -*-
from base.models import DLEditableModel

from django.db import models
from django.conf import settings


class AbstractColor(DLEditableModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=32)
    rgb = models.CharField(max_length=16)
    position = models.FloatField(default=0)

    class Meta:
        abstract = True

class ColorGroup(AbstractColor):
    class Meta:
        db_table = 'dl_color_group'

class Color(DLEditableModel):
    group = models.ForeignKey('ColorGroup', related_name="colors")
    class Meta:
        db_table = 'dl_color'

class AbstractSize(DLEditableModel):
    name = models.CharField(max_length=32)
    position = models.FloatField(default=0)

    class Meta:
        abstract = True

class SizeGroup(AbstractSize):
    class Meta:
        db_table = 'dl_size_group'

class Size(AbstractSize):
    group = models.ForeignKey('SizeGroup', related_name="sizes")

    class Meta:
        db_table = 'dl_size'
