from django.urls import path
from khoj_the_search import views

urlpatterns = [
    path("", views.khoj, name="home"),
]
