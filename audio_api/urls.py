from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('saveaudio/', views.audio_save, name='saveaudio'),
    path('split/<str:id>', views.spleet, name='spleet')

]