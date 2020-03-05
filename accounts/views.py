from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("The Username has been taken")
            elif User.objects.filter(email=email).exists():
                print("The email exists in the Database already")
            else:
                user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username,  password=password1, email=email)
                user.save();
                print('User created')
            return redirect('/')
        else:
            print("The password is not matching")
            return redirect('/')
    return render(request, 'register.html')
