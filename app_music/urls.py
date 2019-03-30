from django.urls import path
from . import views

app_name='app_music'
urlpatterns = [
    path('albums', views.home, name='home'),
    path('albums/?P<int:album_id>', views.album_detail, name = 'album_detail'),
]
