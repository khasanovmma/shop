from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .models import User
from .forms import UserRegisterForm, UserLoginForm


def user_from(request):
    context = {
        "login_form": UserLoginForm(),
        "register_form": UserRegisterForm()
    }
    return render(request, "members/user_form.html", context=context)


def user_register(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("user_form")
        messages.error(
            request, f"Unsuccessful registration. Invalid information.\n\n{form.error_messages}")

    context = {
        "login_form": UserLoginForm(request.POST),
        "register_form": UserRegisterForm()
    }

    return render(request, "members/user_form.html", context=context)


def user_login(request):
    form = UserLoginForm(request.POST)
    if form.is_valid():
        User.objects.get(username=form.POST.username)
        login(request, user)
        return redirect("home")
    else:
        messages.error(request, f"Error:\n\n{form.error_messages}")
        return redirect('user_form')
