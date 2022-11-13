from xml.etree.ElementInclude import include
from django.urls import path

# from ViewHub.UserProfile.views import UserProfile
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('upload/', views.Upload, name='upload'),
	path('login',views.Login,name='login'),
	path('signup/',views.handleSignup,name='Signup'),
	path('',views.handleSignup,name='home'),
	path('token',views.token_send,name='token'),
	path('logout',views.handle_logout,name='logout'),
	path('verify/<auth_token>' , views.verify , name="verify"),
	path('error' , views.error_page , name="error"),
	path('contact' , views.Contact_us , name="contact"),
	path('about/' , views.about , name="about"),
	path('favs/<int:pId>', views.favs, name='favs'),
	path('playlist/<int:playId>/<int:postId>',  views.AddPostToPlaylist, name='AddPostToPlaylist'),
	# path(r'^posts/(?P<pId>[0-9]+)', views.Post, name='Post'),
	path('posts/<int:pId>', views.Post, name='Post'),
]