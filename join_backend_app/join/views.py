from django.shortcuts import render
from rest_framework import generics
from join_backend_app.models import Contact_info, AllTasks, SortTasks, Summary, Data
from .serializers import Contact_infoSerializer, TasksSerializer, SummarySerializer, DataSerializer, SortTasksSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404



class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    def list(self, request):
        serializer = DataSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = get_object_or_404(self.queryset, pk=pk)
        serializer = DataSerializer(product)
        return Response(serializer.data)
        
    def create(self, request):
        serializer = DataSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def destroy(self, request, pk=None):
        data = get_object_or_404(self.queryset, pk=pk)
        serializer = DataSerializer(data)
        data.delete()
        return Response(serializer.data)

class Contact_infoView(generics.ListCreateAPIView):
    queryset = Contact_info.objects.all()
    serializer_class = Contact_infoSerializer
    
class Contact_infoViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact_info.objects.all()
    serializer_class = Contact_infoSerializer
    
class AllTasksView(generics.ListCreateAPIView):
    queryset = AllTasks.objects.all()
    serializer_class = TasksSerializer
    
class AllTasksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AllTasks.objects.all()
    serializer_class = TasksSerializer
    
class SortTasksView(generics.ListCreateAPIView):
    queryset = SortTasks.objects.all()
    serializer_class = SortTasksSerializer
    
class SortTasksViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SortTasks.objects.all()
    serializer_class = SortTasksSerializer
    
class SummaryView(generics.ListCreateAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer
    
class SummaryViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer