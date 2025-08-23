from django.contrib import admin
from .models import Category, Todo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'status', 'due_date', 'completed_at', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'category', 'due_date')
    ordering = ('due_date',)