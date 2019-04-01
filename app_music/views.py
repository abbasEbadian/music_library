from django.shortcuts import render, redirect
from . import models
from accounts import views as ac_views
from django.contrib import messages
# Create your views here.

def home(request,**kwargs):
    context ={
        'albums' : models.Album.objects.all(),
        **kwargs,
        'hello' : 1,
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


def to_albums(request):
    return redirect('app_music:home')
