# accounts/views.py
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm

def signup(request):
    if request.method == "POST":
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            return redirect("login")
    else:
        signup_form = CustomUserCreationForm()
    return render(request, "signup.html", {"form": signup_form})

@login_required
def user_logout(request):
    logout(request)
    return redirect("home")
