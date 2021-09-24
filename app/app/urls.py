
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("khoj_the_search.urls")),

    # API Endpoints
    path("api/user/", include("user.api.urls")),
]
