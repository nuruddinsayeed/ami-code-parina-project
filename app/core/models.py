from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManger(BaseUserManager):
    """By default Django uses username to create account but I am goint to use
    email insted of it. that's why using custom user extending Djangos default
    User model"""
    """Also It provides the helper fucnitons for creating a user/superuser"""

    def create_user(self, email, password=None, **extra_fields):
        """Create a new user to our user model"""

        if not email:
            raise ValueError("User Can't be created without email address")

        user = self.model(email=self.normalize_email(
            email), **extra_fields)
        # using set_pass method for password encription
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and save a noew superuser"""

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user Model that uses django default user model but use email
    insted of username"""

    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD = 'email'  # replace username field with email field
