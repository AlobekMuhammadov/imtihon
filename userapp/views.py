from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .models import *

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')

class RegisterView(View):
    def post(self,request):
        if request.user.is_authenticated:
            Foydalanuvchi.objects.create(
                ism = request.POST.get('ism'),
                yosh = request.POST.get('yosh'),
                kasb = request.POST.get('kasb'),
                user = request.user,
            )
            return redirect('login')

    def get(self,request):
        return render(request,'register.html')


class RegisterTwoView(View):
    def post(self,request):
        User.objects.create_user(
            username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        return redirect('register')

    def get(self,request):
        return render (request,'register2.html')


class LoginView(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        user= authenticate (
            username = request.POST.get('username'),
            password = request.POST.get('password'),
        )
        if user is None:
            return redirect('login')
        login(request,user)
        return redirect('blog')



