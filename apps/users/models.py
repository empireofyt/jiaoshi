# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    nike_name = models.CharField(max_length=50, verbose_name=u"姓名")
    gender = models.CharField(max_length=10, choices=(("male", u'男'), ("female", u'女')), default="female")
    mobile = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username