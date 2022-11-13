# from django.shortcuts import render, HttpResponse, redirect

# # Create your views here.

from pyexpat.errors import messages
from winsound import PlaySound
from django.shortcuts import render
from home.models import upload 
from posts.models import Favs 
from django.contrib import messages
from .models import Playlist
# Create your views here.

def isFav(user, postId):
    return Favs.objects.filter(user=user, postId=postId).exists()
uploads = upload.objects.all()
def UserProfile(request):
    uploads = upload.objects.all()
    suploads = []
    for p in uploads:
        new_p = p
        if isFav(request.user, p.postId):
            new_p.isfav = True 
        print(new_p.isfav)
        suploads.append(new_p)
    context = {
        'uploads' : suploads
    }
    return render(request, 'profile/profile.html', context)

def updateProfile(request):
    return render(request, 'profile/updateProfile.html')

def favorites(request):
    uploads = upload.objects.all()
    suploads = []
    for p in uploads:
        new_p = p
        if isFav(request.user, p.postId):
            new_p.isfav = True 
        suploads.append(new_p)
    context = {
        'uploads' : suploads
    }
    return render(request, 'profile/favorites.html', context)

def playlists(request):
    user_playlist = Playlist.objects.filter(user=request.user)
    context = {
        'playlists' : user_playlist
    }
    return render(request, 'profile/playlists.html', context)

def CreatePlaylist(request):
    if request.method == 'POST':
        name = request.POST['name']
        desc = request.POST['desc']
        if Playlist.objects.filter(Name=name).count() > 0:
            messages.error(request, 'Playlist with this name already exists!')
            return playlists(request)
        new_playlist = Playlist.objects.create(Name=name, description=desc, user=request.user)
        new_playlist.save()
        messages.success(request, 'Your playlist has been created successfully!')
    return playlists(request)

def viewPlaylist(request, playId):
    playlist = Playlist.objects.get(playId=playId)
    postlistt = playlist.list_post.all()
    postlist = []
    for play in postlistt:
        new_play = play
        if isFav(request.user, play.postId):
            new_play.isfav = True 
        postlist.append(new_play)
    context = {
        'playlist':playlist,
        'postlist':postlist
    }
    return render(request, 'profile/playlist.html', context)