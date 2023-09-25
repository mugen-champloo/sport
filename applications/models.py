from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from secrets import randbelow


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=40, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_activation_code(self):
        code = str(randbelow(10000)).zfill(4)
        self.activation_code = code


class TypeOfSport(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="tos_images/%Y/%m/")

class TypeOfPlace(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="top_images/%Y/%m/")

class PriceList(models.Model):
    name = models.CharField(max_length=100)
    text1 = models.CharField(max_length=100)
    text2 = models.CharField(max_length=100)
    text3 = models.CharField(max_length=100)
    price = models.IntegerField()

class Adds(models.Model):
    n_s_p = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    add_title = models.TextField()
    image = models.ImageField(upload_to="adds_images/%Y/%m/")
    description = models.TextField()
    training_rooms = models.TextField()
    adress = models.CharField(max_length=100)
    day = models.DateField()
    time = models.CharField(max_length=100)
    phone_number2 = models.CharField(max_length=100)
    site1 = models.CharField(max_length=100)
    site2 = models.CharField(max_length=100)
    priceList = models.ForeignKey(PriceList, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)