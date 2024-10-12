from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# Briefly, authentication verifies a user is who they claim to be, 
# and authorization determines what an authenticated user is allowed to do.

# 'django.contrib.auth' contains the core of the authentication framework, and its default models.
# 'django.contrib.contenttypes' is the Django content type system, which allows permissions to be associated with models you create.

# SessionMiddleware manages sessions across requests.
# AuthenticationMiddleware associates users with requests using sessions.

# In Python, json.loads() is a method from the json module used to parse a JSON-formatted string into a Python dictionary or object.

# json.loads(request.body) takes the request.body (which is a raw JSON string sent by the frontend) and converts it into a Python dictionary.

@csrf_exempt
def home(request):
    # users = User.objects.all() 
    return HttpResponse('<h1>taufeeq</h1>')

@csrf_exempt
def signup(request):

    if request.method == 'POST':
        # parse JSON body
        try:
            # print('before json: ',request.body)
            data = json.loads(request.body)
            # print('after json: ', data)
            username = data.get('username')
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password') 
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status = 400)

        #check if user already exists
        if not username or not first_name or not last_name or not email or not password:
            return JsonResponse({'error': 'Please fill all the details'}, status = 400) 
        elif User.objects.filter(username = username).exists():
            return JsonResponse({'error': 'This username already exists'}, status = 400)
        elif User.objects.filter(email = email).exists():
            return JsonResponse({'error': 'This email address already exists'}, status = 400)
        else:
            user = User.objects.create(
                username = username,
                email = email,
                password = make_password(password) # hash the password
            )
            user.first_name = first_name
            user.last_name = last_name
            user.save()

            # Return success response
            return JsonResponse({'message': 'Your account has been created successfully'}, status = 200)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)
    

@csrf_exempt
def signin(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username = username , password = password) 

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Successfully logged in :) ', 'user_id':user.id}, status = 200)
        else:
            return JsonResponse({'error': 'No such user :( '})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)


@csrf_exempt
def signout(request):
    logout(request)

    return JsonResponse({'message': 'Successfully logged out :('})