__author__ = 'niels'
from django.shortcuts import render, get_object_or_404, get_list_or_404


def about(request):
    return render(request, 'about.html', context=None)

def cv(request):
    return render(request, 'cv.html', context=None)

def contact(request):
    return render(request, 'contact.html', None)