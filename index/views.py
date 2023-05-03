from django.shortcuts import render, redirect
from .models import Customer
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse
# from random import shuffle


# EMAIL

# @login_required(login_url='signup')
def home(request):
    """
    homepage (no chapter or section)
    """

    context = {}

    return render(request, 'main.html', context)


# @login_required(login_url='signup')
def thanks(request):
    """
    homepage (no chapter or section)
    """

    context = {}

    return render(request, 'thanks.html', context)


def signup(request):
    """
    homepage (no chapter or section)
    """

    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_object = Customer(name=name, email=email, password=password)
        my_object.save()
        return redirect('thanks')
    else:
        return render(request, 'signup.html', context)

