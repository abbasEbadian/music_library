from django.urls import path
from . import views
from accounts import views as ac_views
from django.contrib.auth import views as auth_views

app_name='app_music'
urlpatterns = [
    path('',views.to_albums, name='to_albums'),
    path('albums', views.home, name='home'),
    path('albums/<int:album_id>', views.album_detail, name = 'album_detail'),
    path('register/', ac_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
    path('profile/', ac_views.profile, name='profile'),

]
