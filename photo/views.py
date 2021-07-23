from django.shortcuts import render
from photo.models import Photo

def home(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo/list.html', context)