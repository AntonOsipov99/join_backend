from django.contrib import admin
from .models import Contacts, AllTasks

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'contacts')

@admin.register(AllTasks)
class AllTasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'allTasks') 