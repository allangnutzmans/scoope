from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from .views import main
from laminas.views import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('laminas/<int:laminas_id>/', detail, name='laminas')
    ]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
