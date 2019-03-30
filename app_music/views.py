from django.shortcuts import render
from . import models
# Create your views here.

def home(request):
    context ={
        'albums' : models.Album.objects.all()
        }
    return render(request, 'app_music/home.html',context)

def album_detail(request, album_id):
    album = models.Album.objects.get(id = album_id)
    context ={
        'album' : album,
        'tracks_count': album.track_set.all().count(),
        'tags':album.tags.all()
        }
    return render(request, 'app_music/album_detail.html', context)
