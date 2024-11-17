from django.db import models

class Contact_info(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.DecimalField(max_digits=100, decimal_places=0)
    
    def __str__(self):
        return self.name
    
class Tasks(models.Model):
    title = models.TextField()
    description = models.TextField()
    assigned_to = models.TextField()
    category = models.TextField()
    due_date = models.DateTimeField()
    prio = models.TextField()
    subtasks = models.TextField()
    
    def __str__(self):
        return self.name
    
class Summary(models.Model):
    to_do = models.DecimalField(max_digits=100, decimal_places=0)
    done = models.DecimalField(max_digits=100, decimal_places=0)
    urgent = models.DecimalField(max_digits=100, decimal_places=0)
    tasks_in_board = models.DecimalField(max_digits=100, decimal_places=0)
    tasks_in_progress = models.DecimalField(max_digits=100, decimal_places=0)
    awaiting_feedback = models.DecimalField(max_digits=100, decimal_places=0)
    
    def __str__(self):
        return self.name