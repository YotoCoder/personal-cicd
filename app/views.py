import os
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    
    return render(request, 'index.html')

def start(request):

    o = os.popen('cd .. && cd backend && sudo docker-compose up -d').read()
    print(o)
    return HttpResponseRedirect('/')

@login_required
def stop(request):
    o = os.popen('cd .. && cd backend && sudo docker-compose stop').read()
    print(o)
    return HttpResponseRedirect('/')

@login_required
def restart(request):
    
    o = os.popen('cd .. && cd backend && sudo docker-compose restart').read()
    print(o)
    return HttpResponseRedirect('/')

@login_required
def pull(request):

    o = os.popen('cd .. && cd backend && sudo docker-compose stop && sudo git pull && sudo docker-compose up -d').read()

    print(o)
    return HttpResponseRedirect('/')

@login_required
def update(request):

    o = os.popen('cd .. && cd backend && sudo docker-compose stop && sudo git pull && sudo docker-compose up -d').read()

    print(o)
    return HttpResponseRedirect('/')