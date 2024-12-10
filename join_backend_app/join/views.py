from rest_framework import generics
from join_backend_app.models import Contacts, AllTasks
from .serializers import ContactsSerializer, TasksSerializer

class ContactsView(generics.ListCreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    
class ContactsViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    
class AllTasksView(generics.ListCreateAPIView):
    queryset = AllTasks.objects.all()
    serializer_class = TasksSerializer
    
class AllTasksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllTasks.objects.all()
    serializer_class = TasksSerializer