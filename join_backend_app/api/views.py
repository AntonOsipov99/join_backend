from rest_framework import generics
from join_backend_app.models import Contact, Task
from .serializers import ContactsSerializer, TasksSerializer

class ContactsView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    
class ContactsViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer
    
class AllTasksView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    
class AllTasksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer