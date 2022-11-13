from django.urls import path

# from ViewHub.UserProfile.views import UserProfile
from . import views

urlpatterns = [
    path('', views.create, name='create'),
]
