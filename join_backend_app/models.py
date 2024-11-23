from django.db import models

class Contact_info(models.Model):
    contacts = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.contacts)
    
class AllTasks(models.Model):
    allTasks = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.allTasks)
    
class SortTasks(models.Model):
    sortTasks = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.sortTasks)
    
class Summary(models.Model):
    summary = models.JSONField(default=list, blank=True)
    
    def __str__(self):
        return str(self.summary)
    
class Data(models.Model):
    allTasks = models.JSONField(blank=True, null=True)
    contacts = models.JSONField(blank=True, null=True)
    summary = models.JSONField(blank=True, null=True)
    
#     {
#  "title": "Programmieren",
#  "description": "Vollgas",
#  "assigned_to": "Bobby",
#  "category": "Development",
#  "due_date": 11/23/2024,
#  "prio": "urgent",
#  "subtasks": "Eine kleine Aufgabe"
# }

# assignedShortValues = models.JSONField(blank=True, null=True)
#     assignedToColors = models.JSONField(blank=True, null=True)
#     assignedToValues = models.JSONField(blank=True, null=True)
#     categoryColors = models.JSONField(blank=True, null=True)
#     createdAt = models.CharField
#     description_text = models.TextField()
#     id = models.CharField
#     inWhichContainer = models.CharField
#     priority = 
#     title = models.TextField()
#     assigned_to = models.TextField()
#     category = models.TextField()
#     due_date = models.DateTimeField()
#     prio = models.TextField()
#     subtasks = models.JSONField(blank=True, null=True)

# title = models.TextField()
    # description = models.TextField()
    # assigned_to = models.TextField()
    # category = models.TextField()
    # due_date = models.DateTimeField()
    # prio = models.TextField()
    # subtasks = models.JSONField(blank=True, null=True)