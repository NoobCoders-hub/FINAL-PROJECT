from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from assessment import urls

urlpatterns = [
    path('', views.home, name= 'home'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('register/', views.register, name='register'),
    path('pprofile/', views.pprofile, name='pprofile'),
    path('dprofile/', views.dprofile, name='dprofile'),
]