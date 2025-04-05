from rest_framework import serializers
from join_backend_app.models import Contact, Task

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        exclude = []
        
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = []