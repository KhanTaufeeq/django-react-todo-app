from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Briefly, authentication verifies a user is who they claim to be, 
# and authorization determines what an authenticated user is allowed to do.

# 'django.contrib.auth' contains the core of the authentication framework, and its default models.
# 'django.contrib.contenttypes' is the Django content type system, which allows permissions to be associated with models you create.

# SessionMiddleware manages sessions across requests.
# AuthenticationMiddleware associates users with requests using sessions.

@csrf_exempt
def home(request):
    # users = User.objects.all() 
    return HttpResponse('<h1>taufeeq</h1>')

@csrf_exempt
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password'] 


        user = User.objects.create_user(username, email, password) 

        user.first_name = first_name
        user.last_name = last_name

        if User.objects.filter(username = username).first():
            messages.error(request, 'User name already exists')
            return HttpResponseRedirect('/user/signup/')
        else:
            user.save()
            messages.success(request, "Your account has been successfully created:)")
            return redirect('signin')
    return HttpResponseRedirect('/user/signup/')
    

@csrf_exempt
def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = authenticate(request, username = username , password = password) 

        if user is not None:
            login(request, user)
            messages.success(request, 'Thank you for signing in')
            return redirect('home')
        else:
            messages.error(request, 'Something is went wrong')
            return redirect('signup')
    return HttpResponseRedirect('/user/signup/') 


@csrf_exempt
def signout(request):
    logout(request)
    messages.success(request, 'Successfully logged out') 

    return redirect('signin')


