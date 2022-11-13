from dataclasses import field
from logging import PlaceHolder
from tkinter.tix import Select
from django import forms
from django.forms import ModelForm,TextInput,FileInput,Select
from home.models import upload

class UploadForm(forms.ModelForm):
    class Meta:
        model = upload
        labels = {
            'Title': 'Title of The Post',
            'file': 'Attach Media',
            'description':'Add Description of The Post',
            'Tag':'Add Tag for The Post',
            'private':'Private'
        }
        fields = ['Title', 'file', 'description', 'Tag', 'private']
        # widgets = {
        #     'Title': TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Title of the video',
        #         'style': 'max-width: 300px;',
        #     }),
        #     'file': FileInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Title of the video',
        #         'style': 'max-width: 300px;',
        #     }),
        #     'description': TextInput(attrs={
        #         'class': "form-control",
        #         'placeholder': 'Title of the video',
        #         'style': 'max-width: 300px;',
        #     }),
        #     'Tag': Select(attrs={
        #         'style': 'max-width: 300px;',
        #         c
        #     }),
        # }
