from django.urls import path
from django.contrib.auth import views as auth_view
from .views import register
from . import views

app_name = 'accounts'

urlpatterns = [
   path('register/', register, name='register'),
   path('logout/', auth_view.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
   path('login/', auth_view.LoginView.as_view(), name='login'),
]