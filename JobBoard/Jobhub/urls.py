from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('auth',views.auth, name='auth'),
    path('signup',views.signup, name='signup'),
    path('login',views.login_view, name='login'),
    path('jobs/<int:job_id>',views.job_detail, name='job_detail'),
    path('dashboard',views.dasboard, name='dashboard'),
    path('dash_home',views.dash_home, name='dash_home'),
]