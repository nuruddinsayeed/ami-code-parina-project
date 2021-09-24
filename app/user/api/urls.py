from django.urls import path
from user.api import views


urlpatterns = [
    path("create/", views.CreateUserAPIView.as_view(), name="create-user"),
]
