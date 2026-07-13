from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_date', 'due_date']
    list_filter = ['status', 'created_date','due_date']
    search_fields = ['title', 'description']
    list_editable=['status']
    date_hierarchy = 'created_date'
    ordering = ['-created_date']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'status')
        }),
        ('Dates', {
            'fields': ('created_at', 'due_date')
        }),
        ('Media Files',{
            'fields': ('image', 'file'),
            'classes':('collapse')
        }),
    )

# Register your models here.
