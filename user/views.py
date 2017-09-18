from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate, get_user_model

class LoginView(View):

    def get(self,  request, *args, **kwargs):
        return HttpResponse("hh")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username="dk", password="11223344a")
        django_login(request=self.request, user=user)
        return JsonResponse({"msg": u"用户名或密码错误", "code": 201})

