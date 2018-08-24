from django.shortcuts import render
from .models import Job

def home(request):
    # jobs/home it's because we can have 2 home, it prevents the collision
    # we want to present our instances of Job objects so we must only get this
    # instances from our models and put them into the dict which we return in render

    jobs = Job.objects

    return render(request, 'jobs/home.html', {'jobs': jobs})
