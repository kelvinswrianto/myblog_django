from django.urls import path
from .views import register_view, profile_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', register_view, name='user-register'),
    path('login/', LoginView.as_view(template_name = 'user_login.html'), name='user-login'),
    path('logout/', LogoutView.as_view(template_name = 'user_logout.html'), name='user-logout'),
    path('profile/', profile_view, name='user-profile')
]


