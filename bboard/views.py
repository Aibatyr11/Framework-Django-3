from django.shortcuts import render, redirect

from .models import *

def index_html(request):
    return render(request, 'index.html')


def login_html(request):
    if request.method == 'POST':
        return render(request, 'index.html')
    return render(request, 'login.html')
