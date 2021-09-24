from django.urls import path
from user.api import views


urlpatterns = [
    path("create/", views.CreateUserAPIView.as_view(), name="create-user"),
    path("token/", views.CreateTokenView.as_view(), name="create-token"),
    path("profile/", views.UpdateUserAPIView.as_view(), name="update-profile"),
]
