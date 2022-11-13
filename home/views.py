import imp
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import upload
from posts.models import Favs
from UserProfile.models import Playlist
from django.core import serializers
from django.forms.models import model_to_dict
import json

from .models import profile, contact
# Create your views here.
def isFav(user, postId):
    return Favs.objects.filter(user=user, postId=postId).count() > 0
def home(request):
    uploads = upload.objects.all()
    data = json.dumps(list(upload.objects.values()), default=str)
    context = {}
    if request.user.is_authenticated:
        playlists = Playlist.objects.filter(user=request.user)
        suploads = []
        for p in uploads:
            new_p = p
            print(p.private, p.Title)
            if p.private and p.upload_author != request.user:
                pass 
            if isFav(request.user, p.postId):
                new_p.isfav = True
            suploads.append(new_p)
        context = {
            'uploads' : suploads,
            'playlists': playlists,
            'filter': data
        }
    else:
        uploads = upload.objects.filter(private=0)
        context = {
            'uploads' : uploads, 
            'filter': data
        }
    
    print(data)
    return render(request, 'home.html', context)

def Post(request, pId):
    video = upload.objects.get(postId=pId)
    if isFav(request.user, video.postId):
        video.isfav = True
    context = {
        'post': video
    }
    return render(request, 'post.html', context)

def Upload(request):
    return HttpResponse('hvty')

def favs(request, pId):
    video = upload.objects.get(postId=pId)
    if isFav(request.user, pId):
        Favs.objects.filter(user=request.user, postId=pId).delete()
        msg = "Removed " + "\"" + video.Title + "\" from your favorites!"
        messages.success(request, msg)
    else:
        fav = Favs.objects.create(user=request.user, postId=pId)
        fav.save()
        msg = "Added \"" + video.Title + "\" to your favorites!"
        messages.success(request, msg)
    return home(request)

def AddPostToPlaylist(request, playId, postId):
    playlist = Playlist.objects.get(playId=playId)
    upload_post = upload.objects.get(postId=postId)
    print(playlist.Name)
    print(playlist.list_post.all())
    print(postId)
    print(upload_post.Title)
    if upload_post in playlist.list_post.all():
        msg = "\"" + upload_post.Title + "\" is already exist in \"" + playlist.Name + "\"!"
        messages.error(request, msg)
    else:
        playlist.list_post.add(upload_post)
        playlist.save()
        msg = "\"" + upload_post.Title + "\" is successfully added to \"" + playlist.Name + "\"!"
        messages.success(request, msg)
    return home(request)

def Contact_us(request):

    if request.method == 'POST':
        name = request.POST['name']
        query = request.POST['query']
        email = request.POST['email']
        issue = request.POST['content']
        
        if len(name)<2 or len(email)<10 or len(query)<2 or len(issue)<4:
            messages.error(request, 'Please fill the form Correctly!')

        else:
            messages.success(request, 'Your Query is successfully send to admin!')
            
            b = contact(Name = name,query_related = query, Email = email,Issue = issue)
            b.save()
        # inserting in db
            
    return render(request, 'accounts/contact.html')


def about(request):
    return render(request, 'accounts/about.html')


def handleSignup(request):
    if request.method == 'POST':
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass-1']
        pass2 = request.POST['pass-2']
        

        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'This email is already registered!')

            elif User.objects.filter(username=username).exists():
                print('The email is already taken!')
                messages.error(request,'This username is already registered!')
               
            else:
                myuser = User.objects.create_user(username=username,email=email, password=pass1,first_name=Fname,last_name=Lname)
                auth_token = str(uuid.uuid4())
                profile_obj = profile.objects.create(user=myuser, auth_token=auth_token)
                profile_obj.save()
                myuser.save()
                send_mail_after_registration(email, auth_token)
                return redirect('token')
                # try:
                #     user = authenticate(username=User.objects.get(email=username),password=pass1)
                # except:
                #     user = authenticate(username=username,password=pass1)
                # if user is not None:
                #     login(request,user)
                #     return render(request, 'pay.html')
                # else:
                #     messages.error(request, 'email or password is not matching please create account first')
        else:
            messages.error(request,'Both passwords should be same!')
        
        return redirect('/')
    else:
        return render(request, 'home.html')

def Login(request):
    if request.method == 'POST':
        # get post parameter from the user
        loginemail = request.POST['email']
        loginpassword = request.POST['pass-1']
        myuser = User.objects.filter(email=loginemail).first()
        myprofile = profile.objects.filter(user=myuser).first()
        
        if myuser is None:
            messages.error(request, 'User not found!')
            return redirect('/')

        if not myprofile.is_verfied:
            messages.error(request, 'Your profile is not verified kindly check your Email')
            return redirect('/')

        user = authenticate(username=User.objects.filter(email=loginemail).first(),password=loginpassword)
        if myuser is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('/')
        else:
            messages.error(request,'Invalid username or password, Please try again!')
            return redirect('/')

        

def handle_logout(request):
        logout(request)
        messages.success(request,'Logout Successfully')
        return redirect('/')

def token_send(request):
    messages.success(request, 'Your Account Activation Link has been sent succesfully! Verify your account now!')
    return render(request, 'home.html')


def send_mail_after_registration(email , auth_token):
    subject = 'Your accounts needs to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message, email_from, recipient_list)


def verify(request, auth_token):
    try:
        profile_obj = profile.objects.filter(auth_token = auth_token).first()
        # myuser = User.objects.get(auth_token=auth_token)
        if profile_obj:
            if profile_obj.is_verfied:
                messages.success(request, 'Your account is already verified!')
                return redirect('')
            profile_obj.is_verfied = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/')
        else:
            return redirect('/error')
    except Exception as e:
        return redirect('/')

	
def error_page(request):
    return  render(request , 'accounts/error.html')