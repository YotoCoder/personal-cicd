import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    return render(request, 'index.html')


def start(request):
    os.system('cd .. && cd backend && sudo docker-compose up -d')
    return HttpResponseRedirect('/')


def stop(request):
    os.system('cd .. && cd backend && sudo docker-compose stop')
    return HttpResponseRedirect('/')

def restart(request):
    os.system('cd .. && cd backend && sudo docker-compose restart')
    return HttpResponseRedirect('/')


def pull(request):
    os.system('cd .. && cd backend && sudo docker-compose stop && sudo git pull && sudo docker-compose up -d')
    return HttpResponseRedirect('/')
