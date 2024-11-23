from django.urls import include, path
from .views import Contact_infoView, Contact_infoViewDetail, DataViewSet, AllTasksView, AllTasksViewDetail, SummaryView, SummaryViewDetail, SortTasksView, SortTasksViewDetail
from rest_framework import routers


# router = routers.SimpleRouter()
# router.register(r'data', DataViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('contacts/', Contact_infoView.as_view()),
    path('contacts/<int:pk>/', Contact_infoViewDetail.as_view()),
    path('allTasks/', AllTasksView.as_view()),
    path('allTasks/<int:pk>/', AllTasksViewDetail.as_view()),
    path('sortTasks/', SortTasksView.as_view()),
    path('sortTasks/<int:pk>/', SortTasksViewDetail.as_view()),
    path('summary/', SummaryView.as_view()),
    path('summary/<int:pk>/', SummaryView.as_view()),
]
