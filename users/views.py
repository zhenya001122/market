from django.shortcuts import render, redirect, HttpResponse

from django.contrib import messages
from users.forms import RegisterForm, LoginForm, CustomUserCreationForm
from django.contrib.auth import logout, login, authenticate




def register(request):
    # if request.user.is_authenticated:
    #     return redirect("/")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Создан аккаунт {email}!')
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect("/")

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request=request, **form.cleaned_data)
            if user is None:
                return HttpResponse("Введите корректные данные", status=400)
            login(request, user)
            return redirect("/")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")
