from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login_page'),
    path('logout/', views.userlogout, name='logout_page'),
    path('register/', views.registerpage, name='register_page'),
    path('upload/', views.uploadpage, name='upload_page'),
    path('add/', views.uploadsubtitles, name='upload_subtitles'),
    path('movie/<str:pk>/', views.movieview, name='movie'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)