from django.urls import path
from core import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login_page'),
    path('logout/', views.userlogout, name='logout_page'),
    path('register/', views.registerpage, name='register_page'),
    path('upload/', views.uploadpage, name='upload_page'),

]
