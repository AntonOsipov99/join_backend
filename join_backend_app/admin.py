from django.contrib import admin
from .models import Contact, Task

@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'email', 'phone')

@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title', 
        'task_category', 
        'priority', 
        'created_at', 
        'in_which_container'
    )
    list_filter = ('task_category', 'priority', 'created_at')
    search_fields = ('title', 'description_text', 'task_id')