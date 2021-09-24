from django.urls import path

from khoj_the_search.api import views


urlpatterns = [
    path("", views.InputValuesAPIView.as_view())
]
