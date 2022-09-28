import os
from django.shortcuts import render
from django.http import HttpResponseRedirect     

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def start(request):

    os.popen('cd .. && cd backend && sudo docker-compose up -d').read()

    return HttpResponseRedirect('/')


def stop(request):

    os.popen('cd .. && cd backend && sudo docker-compose stop').read()

    return HttpResponseRedirect('/')

def restart(request):
    
    os.popen('cd .. && cd backend && sudo docker-compose restart').read()

    return HttpResponseRedirect('/')

def pull(request):

    os.popen('cd .. && cd backend && sudo docker-compose stop && sudo git pull && sudo docker-compose up -d').read()

    return HttpResponseRedirect('/')
