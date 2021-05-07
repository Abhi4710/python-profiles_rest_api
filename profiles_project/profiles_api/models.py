from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user model"""

    def create_user(self, email, name, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError("user must have an email address!")

        """"normalizing email"""
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        """Using base function to save password. this will hash the """
        password = user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database models for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    """Required by default no need to mention in rquired field"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retreive full name of user"""
        return self.name

    def get_short_name(self):
        """retreive short name of user"""
        return self.name

    def __str__(self):
        """retunr string representation of our user"""
        return self.email
