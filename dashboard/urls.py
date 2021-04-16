from django.urls import path
from django.contrib.auth import views as auth_views
from .app_views import views
from django.conf import settings
from django.conf.urls.static import static
import notifications.urls

app_name = 'dashboard'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('app/<slug:slug>', views.OpenApp.as_view(), name='open-app')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
