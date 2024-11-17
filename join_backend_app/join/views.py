from django.shortcuts import render
from rest_framework import generics
from join_backend_app.models import Contact_info, Tasks, Summary
from .serializers import Contact_infoSerializer, TasksSerializer, SummarySerializer

class Contact_infoView(generics.ListCreateAPIView):
    queryset = Contact_info.objects.all()
    serializer_class = Contact_infoSerializer
    
class Contact_infoViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact_info.objects.all()
    serializer_class = Contact_infoSerializer
    
class TasksView(generics.ListCreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
class TasksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    
class SummaryView(generics.ListCreateAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    
class SummaryViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer