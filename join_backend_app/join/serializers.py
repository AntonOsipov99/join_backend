from rest_framework import serializers
from join_backend_app.models import Contact_info, Tasks, Summary

class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_info
        exclude = []
        
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        exclude = []
        
class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        exclude = []