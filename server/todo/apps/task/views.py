from django.shortcuts import render
from . models import Task
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import json

# Create your views here.

# @csrf_exempt
# def home(request):
#     tasks = Task.objects.all()
#     return HttpResponse(tasks)

@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        task = json.loads(request.body)
        title = task.get('title')
        body = task.get('body')
        user = request.user
        # user = request.user

        if user.is_authenticated:
            if title:
                task = Task.objects.create(title = title, body = body, user=user)
                task.save()
                return JsonResponse({'message' : 'Your task is added successfully :)'}, status = 200)
            else:
                return JsonResponse({'error' : 'Title is required'}, status = 400)
        
        else:
            return JsonResponse({'error' : 'This user is not authenticated :('})
        
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)
    

@csrf_exempt
def list_tasks(request, user_id):
    try:
        user = User.objects.get(id = user_id)
        tasks = Task.objects.filter(user = user) 
        tasks_list = list(tasks.values('title','body'))
        return JsonResponse({'tasks' : tasks_list}, status = 200)
    
    except User.DoesNotExist:
        return JsonResponse({'error' : "User not found"}, status = 404)


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
