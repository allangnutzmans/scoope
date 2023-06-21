from django.urls import path
from . import views
from .views import detail

app_name = "laminas"
urlpatterns = [
    #path('', views.main, name='main'),
    path('<int:laminas_id>/', views.detail, name='detail'),
    #path('<int:laminas_id>/', detail.as_view()),
]
