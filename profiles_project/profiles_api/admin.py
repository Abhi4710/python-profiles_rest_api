from django.contrib import admin
from .models import UserProfile

"""Tells Django know to register our model on the admin site."""
admin.site.register(UserProfile)
