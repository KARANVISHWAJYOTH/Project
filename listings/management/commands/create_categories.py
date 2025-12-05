from django.core.management.base import BaseCommand
from listings.models import Category


class Command(BaseCommand):
    help = 'Creates default categories for the marketplace'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Laptops', 'icon': '💻', 'slug': 'laptops'},
            {'name': 'Phones', 'icon': '📱', 'slug': 'phones'},
            {'name': 'Cars', 'icon': '🚗', 'slug': 'cars'},
            {'name': 'Furniture', 'icon': '🪑', 'slug': 'furniture'},
            {'name': 'Electronics', 'icon': '📺', 'slug': 'electronics'},
            {'name': 'Clothing', 'icon': '👕', 'slug': 'clothing'},
            {'name': 'Books', 'icon': '📚', 'slug': 'books'},
            {'name': 'Sports', 'icon': '⚽', 'slug': 'sports'},
            {'name': 'Toys', 'icon': '🧸', 'slug': 'toys'},
            {'name': 'Home & Garden', 'icon': '🏡', 'slug': 'home-garden'},
            {'name': 'Other', 'icon': '📦', 'slug': 'other'},
        ]

        created_count = 0
        for cat_data in categories:
            category, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name': cat_data['name'],
                    'icon': cat_data['icon']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created category: {category.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Category already exists: {category.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'\nSuccessfully created {created_count} new categories!')
        )





