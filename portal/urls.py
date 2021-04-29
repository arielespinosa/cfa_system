from django.urls import path
from .app_views import portal as view_portal


app_name = 'portal'

urlpatterns = [
    path('', view_portal.IndexView.as_view(), name='index'),

]
