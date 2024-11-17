from django.urls import path
from .views import Contact_infoView, Contact_infoViewDetail, TasksView, TasksViewDetail, SummaryView, SummaryViewDetail

urlpatterns = [
    path('contact_info/', Contact_infoView.as_view()),
    path('contact_info/<int:pk>/', Contact_infoViewDetail.as_view()),
    path('tasks/', TasksView.as_view()),
    path('tasks/<int:pk>/', TasksViewDetail.as_view()),
    path('summary/', SummaryView.as_view()),
    path('summary/<int:pk>/', SummaryView.as_view()),
]
