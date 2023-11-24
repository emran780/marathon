from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Run  # Import your models

from django.http import HttpResponse





def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')




@login_required
def user_actions(request):
    return render(request, 'user_actions.html')

def past_events(request):
    return render(request, 'past_events.html', {'past_events': Run.objects.all()})

#marathon/views.py
