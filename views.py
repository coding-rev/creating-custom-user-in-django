from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

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
