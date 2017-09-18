from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValueError('The given `phone` must be set.')

        try:
            username = extra_fields.pop('username')
        except KeyError:
            username = phone

        user = self.model(username=username, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, phone, password, **extra_fields):
        return self.create_user(username=username, phone=phone, password=password, is_superuser=True, **extra_fields)

    def get_user(self, user_id):
        try:
            user = self.get(id=user_id)
            return user
        except models.ObjectDoesNotExist:
            return None



class User(AbstractUser):
    identifier = models.CharField(max_length=36, unique=True, default=None, null=True)

    empno = models.CharField(max_length=16, default=None, null=True, db_index=True)

    phone = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']


    @property
    def name_proxy(self):
        if self.first_name:
            return self.first_name
        return self.username