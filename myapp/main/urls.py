from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('warcraft-rc/', views.warcraft_rc, name='warcraft_rc'),
    path('warcraft-ft/', views.warcraft_ft, name='warcraft_ft'),
    path('picture/<slug:pic_slug>/', views.picture_page, name='pic_page'),
    path('pictures/', views.pictures_page, name='pictures_page'),
    path('add/<str:format_add>/', views.add_page, name='add_page'),
    path('audio/', views.audio_page, name='audio_page'),
]
