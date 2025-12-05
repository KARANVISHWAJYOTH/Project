from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'receiver', 'listing', 'sent_at', 'is_read']
    list_filter = ['sent_at', 'is_read']
    search_fields = ['sender__username', 'receiver__username', 'content']





