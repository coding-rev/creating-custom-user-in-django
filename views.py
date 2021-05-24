from django.shortcuts import render, redirect
from django.conf import settings
from .forms import CustomUserCreationForm
from django.contrib import messages


# Create your views here.
def WebsiteRegisterView(response):
    if response.method == "POST":
        form = CustomUserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = CustomUserCreationForm()

    return render(response, "register.html", {"form":form})
