from django.urls import path
from django.contrib.auth import views as auth_views
from .app_views import views
from django.conf import settings
from django.conf.urls.static import static
#import notifications.urls

app_name = 'security'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('account/create/', views.CreateAccount.as_view(), name='create_account'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
