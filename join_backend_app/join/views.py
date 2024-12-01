from rest_framework import generics
from join_backend_app.models import Contacts, AllTasks, Users
from .serializers import ContactsSerializer, TasksSerializer, UsersSerializer

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
    
class UsersView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    
class UsersViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer