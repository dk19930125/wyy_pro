from django.db import models
from django.conf import settings

from base.models import DLEditableModel

from .model_extend import Size, Color
#
class SKU(DLEditableModel):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)

    sizes = models.CharField(max_length=32)
    # size = models.ForeignKey("Size")
    color = models.ForeignKey("Color")

    # created =
