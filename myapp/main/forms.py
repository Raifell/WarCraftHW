from django import forms
from main.models import *


class AddPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('picture', 'game')
        labels = {
            'picture': 'Изображение',
            'game': 'Игра'
        }


class AddAudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ('title', 'audio', 'game')
        labels = {
            'title': 'Название',
            'audio': 'Аудио',
            'game': 'Игра'
        }


class AddVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('format', 'title', 'video', 'game')
        labels = {
            'format': 'Формат видео',
            'title': 'Название',
            'video': 'Видео',
            'game': 'Игра'
        }
