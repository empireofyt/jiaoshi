from django.shortcuts import render

# Create your views here.

# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from .models import UserProfile
# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def login(request):
    if request.method == 'POST':
        user_name = request.POST.get("username", '')
        pass_word = request.POST.get("password", '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或者密码错误！'})
    elif request.method == "GET":
        return render(request, 'login.html', {})


def cuowu1(request):
    return render(request, '403.html', {})


def cuowu2(request):
    return render(request, '404.html', {})


def cuowu3(request):
    return render(request, '500.html', {})


def huodong(request):
    return render(request, 'huodong.html', {})


def index(request):
    return render(request, 'index.html')


def kebiao(request):
    return render(request, 'kebiao.html', {})


def zhuce(request):
    return render(request, 'regist.html', {})


def room(request):
    return render(request, 'room.html', {})


def yuyue(request):
    return render(request, 'yuyue.html', {})


def zhongxin(request):
    return render(request, 'zhongxin.html', {})