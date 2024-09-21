from django.shortcuts import render
from . models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def home(request):
    taks = Task.objects.all()
    return HttpResponseRedirect('/')


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        user = request.user

        if title:
            task = Task.objects.create(user = user, title = title, body = body)
            task.save()
            messages.success(request, "Your task has been created successfully", status = 201)
            return HttpResponseRedirect('/')
        
        else:
            messages.error(request, "title is required", status = 400)
            return HttpResponseRedirect('/add_task')
        
    else:
        messages.error(request, "Invalid request method", status = 405)
        return HttpResponseRedirect('/add_task')
    

def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return HttpResponseRedirect('/')


def edit_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id = task_id)
        task.title = request.POST['title']
        task.body = request.POST['body'] 

        task.save() 

    elif request.method == 'GET':
        task = Task.objects.get(id = task_id)
        return HttpResponseRedirect('/')
