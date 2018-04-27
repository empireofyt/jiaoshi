from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('login/', views.login, name = 'login'),
    path('403/', views.cuowu1, name='cuowu1'),
    path('404/', views.cuowu2, name='cuowu2'),
    path('500/', views.cuowu3, name='cuowu3'),
    path('huodong/', views.huodong, name='huodong'),
    path('kebiao/', views.kebiao, name='kebiao'),
    path('zhuce/', views.zhuce, name='zhuce'),
    path('room/', views.room, name='room'),
    path('yuyue/', views.yuyue, name='yuyue'),
    path('zhongxin/', views.zhongxin, name='zhongxin'),
]