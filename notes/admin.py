from django.contrib import admin
from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'category', 'elect', 'created', 'updated']
    list_filter = ['category', 'created']
    search_fields = ['title', 'owner']
    ordering = ['owner', 'created']
