# _*_ encoding:utf-8 _*_
"""jiaoshi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path,include

#from users import views
#from django.conf.urls import url
from django.contrib import admin
#from django.views.generic import TemplateView
#from users.views import login
#from users.views import cuowu1
#from users.views import cuowu2
#from users.views import cuowu3
#from users.views import huodong
#from users.views import zhuce
#from users.views import index
#from users.views import kebiao
#from users.views import room
#from users.views import zhongxin


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', views.index , name ='zhuye')
    path('', include('users.urls', namespace = 'users'))
    #path('^403/', cuowu1, name='403'),
    #path('login/', login, name='login'),
    #path('zhongxin/', zhongxin, name='zhongxin'),
    #path('kebiao/', kebiao, name='kebiao'),
   # path('regist/', zhuce, name='zhuce'),
   # path('room/', room, name='room'),
   # path('huodong/', huodong, name='huodong'),
   # path('404/', cuowu2, name='404'),
   # path('500/', cuowu3, name='500'),
]

