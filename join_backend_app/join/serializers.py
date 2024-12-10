from rest_framework import serializers
from join_backend_app.models import Contacts, AllTasks

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        exclude = []
        
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllTasks
        exclude = []