from django.contrib import admin
from gas_app import views 
from django.urls import include, path 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('sign_up/', views.sign_up, name='sign_up'),
    path('create_request/', views.create_request, name='create_request'),
    path('user_requests/', views.user_requests, name='user_requests'),
    path('support_dashboard/', views.support_dashboard, name='support_dashboard'),
    path('', include(('gas_app.urls', 'gas_app'), namespace='gas_app')),
     path('accounts/', include('django.contrib.auth.urls')),
]
