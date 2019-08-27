from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
	re_path(r'^', include('applications.home.url')),
	re_path(r'^', include('applications.biblioteca.url')),
    re_path('admin/', admin.site.urls),
]