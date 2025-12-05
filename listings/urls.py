from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('category/<slug:slug>/', views.category_listings, name='category_listings'),
    path('listing/<int:pk>/', views.listing_detail, name='listing_detail'),
    path('create/', views.create_listing, name='create_listing'),
    path('edit/<int:pk>/', views.edit_listing, name='edit_listing'),
    path('delete/<int:pk>/', views.delete_listing, name='delete_listing'),
    path('search/', views.search_listings, name='search'),
    path('my-listings/', views.my_listings, name='my_listings'),
]





