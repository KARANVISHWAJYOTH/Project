from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('user/<int:user_id>/listing/<int:listing_id>/', views.chat_detail, name='chat_detail_with_listing'),
    path('user/<int:user_id>/', views.chat_detail, name='chat_detail'),
    path('start/<int:listing_id>/', views.start_chat, name='start_chat'),
]

