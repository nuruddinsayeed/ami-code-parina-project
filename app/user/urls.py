from django.urls import path

from user import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.RegistrationView.as_view(), name="register")
]
