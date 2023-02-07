from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from .models import audio_storage


class AudioForm(forms.ModelForm):
    class Meta:
        model = audio_storage
        fields = ['file_name','audio_file']
    file_name = forms.CharField(widget = forms.TextInput(attrs={'class':'form-control'}))
    audio_file = forms.FileField(widget = forms.FileInput(attrs={'class': 'form-control','accept': 'audio/*'}))
