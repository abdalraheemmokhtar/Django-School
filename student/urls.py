from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.student, name='student'),
    path('register/', views.register, name='register'),
    path('cus/', views.home_view, name='home_view'),
    path('perform_login', views.perform_login, name='perform_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
]