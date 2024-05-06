from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('fail')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('fail')
        else:
            return render(request, "account/login.html")
    else:
        return render(request, "account/login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password != repassword:
            return render(request, "account/register.html", {"error": "parola eşleşmiyor"})

        if User.objects.filter(username=username):
            return render(request, "account/register.html", {"error": "kullanıcı adı kullanılıyor"})

        if User.objects.filter(email=email):
            return render(request, "account/register.html", {"error": "email adresi kullanılıyor"})
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')


    else:
        return render(request, "account/register.html")


def logoutUser(request):
    logout(request)
    return redirect('logout')


def fail(request):
    return render(request, "account/fail.html")
