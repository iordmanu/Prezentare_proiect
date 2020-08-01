from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            next_url =request.GET.get('redirect_to', reverse('users:profile'))
            return HttpResponseRedirect(reverse('users:profile'))
        next_url = request.GET.get('next', '')
        return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:login'))

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    return render(request, 'users/index.html', {})

@login_required
def index(request):
    return render(request, 'users/index.html', {})


# Create your views here.
