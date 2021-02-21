from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Logged with success!')
        else:
            messages.error(request, 'Not a valid email!')
            return redirect('register')
        return redirect('dashboard')

    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        second_password = request.POST['secondPassword']

        if empty_field(first_name) or empty_field(last_name):
            messages.error(request, 'First and last names are required!')
            return redirect('register')
        if empty_field(username) or empty_field(email):
            messages.error(request, 'Username and email are required!')
            return redirect('register')
        if empty_field(password):
            messages.error(request, 'Password can\'t be empty!')
            return redirect('register')
        if not_equal_passwords(password, second_password):
            messages.error(request, 'Passwords don\'t match!')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('register')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Account registered!')
        return redirect('dashboard')
    return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    return render(request, 'dashboard.html')

def empty_field(field):
    return not field.strip()

def not_equal_passwords(password, second_password):
    return password != second_password