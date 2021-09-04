from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, phone_number,
                    username, password,
                    **other_fileds):
        if not email:
            raise ValueError('Incorrect email')

        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number,
                          username=username, **other_fileds)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, phone_number,
                    username, password,
                    **other_fileds):
        other_fileds.setdefault('is_staff', True)
        other_fileds.setdefault('is_superuser', True)
        other_fileds.setdefault('is_active', True)

        return self.create_user(email, phone_number,
                    username, password, **other_fileds)

class User(AbstractBaseUser, PermissionsMixin):
    # TODO: add no_spaces validation to username
    username = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(max_length=100, null=True, unique=True)
    phone_number = models.CharField(max_length=20, null=True, unique=True)
    public_name = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    second_name = models.CharField(max_length=20, null=True, blank=True)
    father_name = models.CharField(max_length=20, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    def __str__(self) -> str:
        return str(self.username) + ' : ' + str(self.public_name)

class Password(models.Model):
    service = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.service)
