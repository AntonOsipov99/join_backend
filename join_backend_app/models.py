from django.db import models

class Contacts(models.Model):
    contacts = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.contacts)
    
class AllTasks(models.Model):
    allTasks = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.allTasks)
    
class Users(models.Model):
    users = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.users)