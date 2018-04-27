# _*_ encoding:utf-8 _*_

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

# Create your models here.


class Activity(models.Model):
    data = models.DateField(verbose_name=u"日期", null=True, blank=True)
    time = models.CharField(choices=(('morning', u'上午'), ('afternoon', u'下午'), ('night', u'晚上')), max_length= 100, default='morning')
    class_num = models.CharField(max_length=10,verbose_name=u"教室", default=0)
    order = models.CharField(max_length=100, verbose_name=u'预约', default=0)

    class Meta:
        verbose_name = u"活动信息"
        verbose_name_plural = verbose_name