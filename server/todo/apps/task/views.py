from django.shortcuts import render
from . models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
# Create your views here.

@csrf_exempt
def home(request):
    tasks = Task.objects.all()
    return HttpResponse(tasks)

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        user = request.user
        # user = request.user

        if user.is_authenticated:
            if title:
                task = Task.objects.create(title = title, body = body, user=user)
                task.save()
                messages.success(request, "Your task has been created successfully")
                return HttpResponseRedirect('/')
        
            else:
                messages.error(request, "title is required")
                return HttpResponseRedirect('/add_task')
        
        else:
            messages.error(request, 'User is not authenticate')
        
    else:
        messages.error(request, "Invalid request method")
        return HttpResponseRedirect('/add_task')
    

@csrf_exempt
def delete_task(request, task_id):
    task = Task.objects.get(id = task_id)
    task.delete()
    return HttpResponseRedirect('/')


@csrf_exempt
def edit_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id = task_id)
        task.title = request.POST['title']
        task.body = request.POST['body'] 
        task.save() 

    elif request.method == 'GET':
        task = Task.objects.get(id = task_id)
        return HttpResponseRedirect('/')
