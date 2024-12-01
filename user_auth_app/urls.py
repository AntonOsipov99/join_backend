from django.urls import include, path

from . import views

urlpatterns = [
    path('join/auth/', include('user_auth_app.api.urls'))
]