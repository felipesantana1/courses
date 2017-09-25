from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def display(request):
    context = {
        'courses' : Courses.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    errors = Courses.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses')
    else:
        x = Courses.objects.create(name = request.POST['name'], desc = request.POST['desc'])
    return redirect('/courses')

def delete(request, id):
    context ={
        'course' : Courses.objects.get(id=id)
    }
    return render(request, 'courses_app/delete.html', context)

def destroy(request, id):
    x = Courses.objects.get(id=id)
    x.delete()
    return redirect('/courses')