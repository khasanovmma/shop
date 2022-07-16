from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from .forms import UserRegisterForm

def register_request(request):

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = UserRegisterForm()
    print(form)

    return render(request, "members/user_form.html", context={"form": form})

