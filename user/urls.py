

from django.conf.urls import url, include
from rest_framework import routers
from .views import LoginView
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^api/login/$', csrf_exempt(LoginView.as_view()), name='api.skus'),

]