from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('register/', views.register_view.as_view(), name = 'register'),
    path('reg_or_auth/', views.reg_or_auth_view, name = 'reg_or_auth'),
    path('profile/<int:pk>', views.profile_view.as_view(), name = 'profile'),
]