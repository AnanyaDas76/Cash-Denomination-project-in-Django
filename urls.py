
from django.contrib import admin
from django.urls import path
from .views import deno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', deno, name = 'cashdeno'),
]
