# -*- coding:utf-8 -*-
__author__ = 'DK'

from django.conf.urls import url, include
from rest_framework import routers
from .views import SKUViewSet
from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register(r'skus', SKUViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls), name='api.skus'),

]