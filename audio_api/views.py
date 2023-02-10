from django.shortcuts import render
from django.http import JsonResponse
from .forms import AudioForm
from .models import audio_storage
from django.views.decorators.csrf import csrf_exempt
from spleeter.separator import Separator
import os


# Create your views here.

def index(request):
    audio_form = AudioForm()
    context = {
        'forms': audio_form
    }
    return render(request,'index.html',context)

def spleet(request,id):
    audio_id = audio_storage.objects.get(id=id)
    audio = audio_id.my_file
    aud = str(audio)
    audio_dir =aud[:-4]
    input_file = f"media\{audio}"
    output_dir = "media\output"
    separator = Separator('spleeter:4stems')
    separator.separate_to_file(input_file,output_dir)
    v = f"..\{output_dir}\{audio_dir}"
    vocals_file = os.path.join(v,'vocals.wav')
    bass_file = os.path.join(v,'bass.wav')
    piano_file = os.path.join(v, 'other.wav')
    drums_file = os.path.join(v, 'drums.wav')
    context = {
        "original":input_file,
        "vocals":vocals_file,
        "bass":bass_file,
        "drums":drums_file,
        "piano":piano_file
    }
    return render(request, 'split.html', context)


@csrf_exempt
def audio_save(request):
    if request.method == 'POST':
        audio_form = AudioForm(request.POST, request.FILES)
        if audio_form.is_valid():
            file_name = audio_form.cleaned_data['file_name']
            audio_file = audio_form.cleaned_data['audio_file']
            audio_storage(file_name=file_name,my_file=audio_file).save()
            uploaded_file = audio_storage.objects.values()
            all_files = list(uploaded_file)
            needed_file = all_files[-1]
            return JsonResponse({"status":"file uploaded succesfully","upload": needed_file})
        else:
            return JsonResponse({"status":"error occured"})
            #uploaded_file = audio_storage.objects.get(my_file=audio_f
