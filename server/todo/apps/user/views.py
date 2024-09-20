from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

# Briefly, authentication verifies a user is who they claim to be, 
# and authorization determines what an authenticated user is allowed to do.

# 'django.contrib.auth' contains the core of the authentication framework, and its default models.
# 'django.contrib.contenttypes' is the Django content type system, which allows permissions to be associated with models you create.

# SessionMiddleware manages sessions across requests.
# AuthenticationMiddleware associates users with requests using sessions.

def home(request):
    users = User.objects.all() 
    return HttpResponseRedirect('/')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password'] 

        user = User.objects.create(username, email, password) 

        user.first_name = first_name
        user.last_name = last_name

        user.save()

        messages.success(request, "Your account has been successfully created:)")

        return redirect('signin')
    return HttpResponseRedirect('/signup')
    

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
    return HttpResponseRedirect('/signup') 


def signout(request):
    logout(request)
    messages.success(request, 'Successfully logged out') 

    return redirect('signin')


