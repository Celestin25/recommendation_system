"""
Users DATABASE MODELS
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """
    Custom UserManager model that manages user profile
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # Remember to restrict user email to only the ALU community emails.
    email = models.EmailField(max_length=255, unique=True)
    short_bio = models.CharField(max_length=255, blank=True)
    about_me = models.TextField(blank=True)
    intake = models.ForeignKey(
        'Intake', on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(
        'Course', on_delete=models.SET_NULL, null=True, blank=True)
    profession = models.CharField(
        max_length=255, blank=True, help_text="Your Profession"
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        """String representation of a user"""
        if self.full_name:
            return f"{self.full_name}"
        return self.email


class Course(models.Model):
    """
    Course model
    """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, )
    duration = models.FloatField(help_text="Duration in years")

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Intake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
