from datetime import datetime, timedelta
from importlib.resources._common import _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from enum import Enum
from rest_framework import serializers


class Address(models.Model):
    position_name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)  # Région, état ou province
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, blank=True, null=True)  # Code postal
    google_maps = models.URLField(blank=True, null=True)
    type_of_address = models.CharField(max_length=10, blank=True, null=True,
                                       choices=(('O', 'Office'), ('H', 'Home'), ('O', 'Other')))

    def __str__(self):
        return f"{self.number} {self.street}, {self.city}, {self.region}, {self.country}"


class CarModel(models.Model):
    make = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    licence_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.make

    def validate_owner(self, owner):
        if self.owner.ProfileCustomUser.role == 'BOTH' or self.owner.ProfileCustomUser.role == 'DRIVER':
            return True
        else:
            return f'{self.owner} must be driver or both to create a car'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        """user_role = extra_fields.pop('user_role', None)
        if user_role == 'driver':
            extra_fields.setdefault('is_driver', True)
            extra_fields.setdefault('is_passenger', False)
        elif user_role == 'passenger':
            extra_fields.setdefault('is_driver', False)
            extra_fields.setdefault('is_passenger', True)
        else:  # Aucun rôle par défaut
            extra_fields.setdefault('is_driver', False)
            extra_fields.setdefault('is_passenger', False)"""
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class UserRole(Enum):
    DRIVER = 'DRIVER'
    PASSENGER = 'PASSENGER'
    BOTH = 'BOTH'


class CustomUser(AbstractBaseUser):
    last_name = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class ProfileCustomUser(models.Model):
    CATEGORIES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birth_date = models.DateField(blank=True, null=True)
    genre = models.CharField(max_length=10, blank=True, null=True, choices=(('F', 'Female'), ('M', 'Male')))
    phone_number = PhoneNumberField(unique=True)
    num_permis = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=10, choices=[(role.value, role.name) for role in UserRole])
    category = models.CharField(max_length=1, choices=CATEGORIES)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='addresses', default=None, blank=True,
                                null=True)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars', default=None, blank=True,
                            null=True)

    date_delivrance = models.DateField(default=timezone.now)
    date_expiration = models.DateField()

    def validate_date_of_birth(self, birth_date=None):
        today = timezone.now().date()
        age = today - birth_date
        min_age = timedelta(days=18 * 365.25)  # 18 années en jours (approximation)

        if age < min_age:
            raise serializers.ValidationError("Vous devez avoir au moins 18 ans pour vous inscrire.")

        return birth_date


class Notification(models.Model):
    pass


class Reclaim(models.Model):
    owner = models.ForeignKey(ProfileCustomUser, on_delete=models.CASCADE, related_name='reclaims')
    date = models.DateField(default=timezone.now)
    reason = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        pass
