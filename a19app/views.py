from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponse

def home(request):
    return render(request,'homepage.html')
def register(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        email=request.POST['em']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return redirect('home')
    else:
        return render(request,'register.html')
def login_user(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse('you are entered incorrect username and password')
    else:
        return render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('home')
