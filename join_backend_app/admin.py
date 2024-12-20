from django.contrib import admin
from django import forms
from .models import Contact, Task
import datetime


@admin.register(Contact)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'color')
    list_filter = ('color',)
    search_fields = ('name', 'email', 'phone')


class TaskAdminForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date', 'min': datetime.date.today().strftime('%Y-%m-%d')})
        }


@admin.register(Task)
class TasksAdmin(admin.ModelAdmin):
    form = TaskAdminForm
    list_display = (
        'id',
        'title',
        'task_category',
        'priority',
        'created_at',
    )
    list_filter = ('task_category', 'priority', 'created_at')
    search_fields = ('title', 'description_text', 'task_id')

    fieldsets = (
        (None, {
            'fields': (
                'title',
                'task_category',
                'category_color',
                'description_text',
                'created_at',
            ),
        }),
    )
