from django.urls import path
from . import views

app_name = "laminas"
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:laminas_id>/', views.detail, name='detail'),
]
