from django.contrib import admin
from .models import Category, Listing, SearchHistory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'owner', 'created_at', 'is_sold']
    list_filter = ['category', 'is_sold', 'created_at']
    search_fields = ['title', 'description', 'owner__username']


@admin.register(SearchHistory)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'query', 'category', 'results_count', 'searched_at']
    list_filter = ['searched_at', 'category']
    search_fields = ['query', 'user__username']
