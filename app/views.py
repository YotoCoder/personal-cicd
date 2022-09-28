import os
from django.shortcuts import render
from django.http import HttpResponseRedirect     

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def start(request):

    o = os.popen('cd .. && cd backend && sudo docker-compose up -d').read()

    print(o)
    return HttpResponseRedirect('/')


def stop(request):

    o = os.popen('cd .. && cd backend && sudo docker-compose stop').read()

    print(o)
    return HttpResponseRedirect('/')

def restart(request):
    
    o = os.popen('cd .. && cd backend && sudo docker-compose restart').read()

    print(o)
    return HttpResponseRedirect('/')

def pull(request):

    o = os.popen('cd .. && cd backend && sudo docker-compose stop && sudo git pull && sudo docker-compose up -d').read()

    print(o)
    return HttpResponseRedirect('/')
