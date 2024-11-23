from rest_framework import serializers
from join_backend_app.models import Contact_info, AllTasks, SortTasks, Summary, Data

class Contact_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_info
        exclude = []
        
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllTasks
        exclude = []
        
class SortTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SortTasks
        exclude = []
        
class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        exclude = []

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        exclude = []