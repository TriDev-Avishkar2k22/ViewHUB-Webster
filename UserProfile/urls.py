from django.urls import path
from . import views

urlpatterns = [
	path('/', views.UserProfile, name ='profile'),
	path('/settings', views.updateProfile, name='settings'),
	path('/favorites', views.favorites, name='favorites'),
	path('/playlists', views.playlists, name='playlists'),
	path('/createPlaylist', views.CreatePlaylist, name='CreatePlaylist'),
	path('/playlists/<int:playId>', views.viewPlaylist, name='viewPlaylist'),
]