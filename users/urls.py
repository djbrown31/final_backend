from django.urls import include, path
from . import views
from django.urls import path
from .views import current_user, UserList

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view())
]

