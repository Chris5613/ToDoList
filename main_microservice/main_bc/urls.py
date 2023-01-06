from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


def redirect_to_home(request):
    return redirect("home")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("main.urls")),
    path("",redirect_to_home),
    path("accounts/", include("accounts.urls")),
]
