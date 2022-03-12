from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from users.forms import RegisterUserForm


def register_view(request):
    """Register user page"""
    if request.user.is_authenticated:
        return redirect('/')

    form = RegisterUserForm()

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            messages.success(
                request, 'User {} registered correctly'.format(username)
            )
            return redirect('/')

    context = {'form': form}
    return render(request, 'pages/register.html', context)


def login_view(request):
    """Login user view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username Or Password is incorrect.')

    context = {}

    return render(request, 'pages/login.html', context)


@login_required(login_url='login')
def logout_view(request):
    """Logout user view"""
    logout(request)
    return redirect('/')
