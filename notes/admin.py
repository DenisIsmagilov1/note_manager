from django.contrib import admin
from .models import Note, Category


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'category', 'elect', 'created', 'updated']
    list_filter = ['category', 'created']
    search_fields = ['title', 'owner']
    ordering = ['owner', 'created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
