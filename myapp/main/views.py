from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import *
from .forms import *


def main_page(request):
    return render(request, 'main/main_page.html', {'title': 'Main Page'})


def warcraft_rc(request):
    text = get_object_or_404(Description, game__title='Warcraft III: Reign of Chaos')
    context = {
        'title': 'Warcraft III: Reign of Chaos',
        'text': text
    }
    return render(request, 'main/warcraft_rc.html', context)


def warcraft_ft(request):
    text = get_object_or_404(Description, game__title='Warcraft III: The Frozen Throne')
    context = {
        'title': 'Warcraft III: The Frozen Throne',
        'text': text
    }
    return render(request, 'main/warcraft_ft.html', context)


def pictures_page(request):
    pictures = Picture.objects.all()
    context = {
        'title': 'Pictures',
        'pictures': pictures
    }
    return render(request, 'main/pictures_page.html', context)


def picture_page(request, pic_slug):
    pic = get_object_or_404(Picture, slug=pic_slug)
    context = {
        'title': 'Pictures',
        'picture': pic
    }
    return render(request, 'main/picture_page.html', context)


def add_page(request, format_add):
    form = None
    if format_add == 'picture':
        form = AddPictureForm()
        if request.method == 'POST':
            form = AddPictureForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('pictures_page')
    elif format_add == 'audio':
        form = AddAudioForm()
        if request.method == 'POST':
            form = AddAudioForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('audio_page')
    elif format_add == 'video':
        form = AddVideoForm()
        if request.method == 'POST':
            form = AddVideoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('videos_page')
    else:
        raise Http404()

    context = {
        'title': 'Add',
        'form': form
    }
    return render(request, 'main/add_page.html', context)


def audio_page(request):
    audios = Audio.objects.all()
    context = {
        'title': 'Audio',
        'audios': audios,
    }
    return render(request, 'main/audio_page.html', context)


def videos_page(request):
    cinematic = Video.objects.filter(format='Cinematic')
    gameplay = Video.objects.filter(format='Gameplay')
    context = {
        'title': 'Videos',
        'gameplay': gameplay,
        'cinematic': cinematic,
    }
    return render(request, 'main/videos_page.html', context)
