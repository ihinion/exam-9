from django import forms
from django.forms import CheckboxSelectMultiple
from webapp.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['author']


class PhotoFormUpdate(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['author', 'picture']
