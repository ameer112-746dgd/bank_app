from django.urls import path
from . import views
from .views import dashboard 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Ensure this line exists
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
]
