from django.shortcuts import render, HttpResponse, redirect
from home.models import upload
from django.contrib import messages
from .forms import UploadForm
# Create your views here.
def create(request):
    if request.method =='POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            Title = form['Title'].value()
            tag = form['Tag'].value()
            desc = form['description'].value()
            private = form['private'].value()
            file = request.FILES['file']
            format = file.content_type
            format = format.split('/')[0]
            p = upload(upload_author = user, file = file, Title = Title, Tag = tag, description = desc, private=private, format=format)
            p.save()
            messages.success(request,'Your post has been successfully uploaded!')
            return redirect('/')
        messages.error(request,'Your post has not been uploaded :(')
        return redirect('/')

    else:
        form = UploadForm()
        context = {
            'form' : form
        }
        return render(request, 'create.html', context)
   