from django.shortcuts import render, redirect
from django.views import View
from userapp.models import *
from .models import *

class BlogView(View):
    def post(self,request):
        if request.user.is_authenticated:
            Maqola.objects.create(
                sarlavha = 's',
                mavzu = 'm',
                sana = 'sa',
                matn = 'ma',
                muallif = request.user,
            )

    def get(self,request):
        if request.user.is_authenticated:
            content = {
                'maqolalar':Maqola.objects.filter(muallif__user=request.user)
            }
            return render(request,'blog.html',content)
        return redirect('login')


