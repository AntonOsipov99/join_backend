from django.urls import path
from .views import ContactsView, ContactsViewDetail, AllTasksView, AllTasksViewDetail, UsersView, UsersViewDetail

urlpatterns = [
    path('contacts/', ContactsView.as_view()),
    path('contacts/<int:pk>/', ContactsViewDetail.as_view()),
    path('allTasks/', AllTasksView.as_view()),
    path('allTasks/<int:pk>/', AllTasksViewDetail.as_view()),
    path('users/', UsersView.as_view()),
    path('users/<int:pk>/', UsersViewDetail.as_view()),
]
