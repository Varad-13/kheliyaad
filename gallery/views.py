from django.shortcuts import render, redirect
from .models import *

def Gallery(request):
    context = {}
    images = Image.objects.all()
    context['images'] = images
    return render(request, 'gallery/gallery.html', context)