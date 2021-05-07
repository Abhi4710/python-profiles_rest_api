from django.contrib import admin
from .models import UserProfile, ProfileFeedItem

"""Tells Django know to register our model on the admin site."""
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
