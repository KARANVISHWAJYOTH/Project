#!/usr/bin/env python
"""Quick test script to verify the setup"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
django.setup()

from django.contrib.auth.models import User
from listings.models import Category, Listing
from chat.models import Message

print("Django setup successful!")
print(f"Categories in database: {Category.objects.count()}")
print(f"Users in database: {User.objects.count()}")
print(f"Listings in database: {Listing.objects.count()}")
print(f"Messages in database: {Message.objects.count()}")
print("\nAll models are working correctly!")
print("\nYou can now run: python manage.py runserver")





