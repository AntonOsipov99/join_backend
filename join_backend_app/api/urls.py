from django.urls import path
from .views import ContactsView, ContactsViewDetail, AllTasksView, AllTasksViewDetail

urlpatterns = [
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', ContactsViewDetail.as_view()),
    path('allTasks/', AllTasksView.as_view()),
    path('allTasks/<int:pk>/', AllTasksViewDetail.as_view()),
]
