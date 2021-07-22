from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user_name = form.cleaned_data.get('username')
                messages.success(request, 'Your Account is Created '+user_name)
                return redirect('/login/')

        context = {'form': form}

        return render(request, 'App/registration.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                messages.info(request, "Incorrect Username or Password")
                return render(request, 'App/login.html')

        return render(request, 'App/login.html')


@login_required(login_url='login')
def home(request):
    return render(request, 'App/home.html')
