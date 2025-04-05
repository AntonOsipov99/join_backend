from django.urls import include, path

from . import views

urlpatterns = [
    path('api/auth/', include('user_auth_app.api.urls'))
]