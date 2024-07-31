# gas_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('create_request/', views.create_request, name='create_request'),
    path('user_requests/', views.user_requests, name='user_requests'),
    path('support_dashboard/', views.support_dashboard, name='support_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='gas_app/login.html'), name='login'),
    path('', views.home, name='home'),
      path('login/', auth_views.LoginView.as_view(), name='login'),
]
