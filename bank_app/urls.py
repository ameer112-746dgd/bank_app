from django.urls import path
from . import views
from .views import dashboard 

urlpatterns = [
    # path('', views.register, name='register'),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Ensure this line exists
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('dashboard/', views.dashboard, name='dashboard'),
    # path('create-account/', views.create_account, name='create_account'),
    # path('view-account/<int:account_id>/', views.view_account, name='view_account'),
    # path('update-account/<int:account_id>/', views.update_account, name='update_account'),
    # path('delete-account/<int:account_id>/', views.delete_account, name='delete_account'),
    # path('create-transaction/<int:account_id>/', views.create_transaction, name='create_transaction'),
]
