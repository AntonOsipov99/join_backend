from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
class Task(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    task_category = models.CharField(max_length=200, null=False, blank=False)
    subtasks_status_array = models.JSONField(null=True, blank=True)
    subtasks_id =  models.JSONField(null=True, blank=True) 
    subtasks =  models.JSONField(null=True, blank=True) 
    progress_bar_id = models.CharField(max_length=50, null=True, blank=True)
    priority = models.JSONField(null=True, blank=True) 
    in_which_container = models.JSONField(null=True, blank=True)
    task_id = models.CharField(max_length=50, null=True, blank=True)
    description_text = models.TextField(null=False, blank=False)
    created_at = models.DateField(null=True)
    category_color = models.CharField(max_length=200, null=False, blank=False)
    assigned_to_values = models.JSONField(null=True, blank=True)
    assigned_to_colors = models.JSONField(null=True, blank=True)
    assigned_short_values = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return str(self.title)