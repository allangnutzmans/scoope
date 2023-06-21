from django.contrib import admin
from django.urls import path, include
from .views import main

urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('laminas/', include('laminas.urls')),
    ]
   