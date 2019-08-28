import json
from email import message

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render

# Create your views here.
from django.utils.safestring import mark_safe


def signup(request) :
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid() :
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,'registration/login.html')
        else :
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm
        return render(request, 'signup.html', {'form': form})

def home(request) :
    if request.user.is_authenticated:
        return render(request, 'home.html')
    return render(request,'registration/login.html')

def index(request):
    if request.user.is_authenticated :
        return render(request, 'index.html', {})
    else :
        return render(request,'registration/login.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })