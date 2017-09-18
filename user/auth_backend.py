import re
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from .models import User


class UserAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            if re.match('^1\d{10}$', username):
                try:
                    user = User.objects.get(phone=username)
                except User.DoesNotExist:
                    return None
            else:
                return None

        # if settings.DEBUG:
        #     return user

        if user.check_password(raw_password=password):
            return user
        else:
            return None