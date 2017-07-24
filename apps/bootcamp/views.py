from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *

def index(request):
    courses = {
        "courses": Course.objects.all()
    }
    return render(request,'bootcamp/index.html', courses)

def add(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags='tag')
            return redirect ('/')
        else:
            Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        return redirect ('/')

def destroy(request, id):
    if request.method == "GET":
        one_course = {
            "course": Course.objects.get(id=id)
        }
        return render(request,'bootcamp/destroy.html', one_course)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect('/')
        else:
            Course.objects.get(id=id).delete()
            return redirect('/')

# Create your views here.
