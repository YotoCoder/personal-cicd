from django.urls import path

from .views import home, start, restart, stop, pull
urlpatterns = [
    path('', home, name='home'),
    path('start/', start, name='start'),
    path('stop/', stop, name='stop'),
    path('restart/', restart, name='restart'),
    path('pull/', pull, name='pull'),
]