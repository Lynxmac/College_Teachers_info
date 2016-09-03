#-*-coding:utf-8-*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(verbose_name = '姓名' ,max_length=30,default='')
    sex_choice = (("Male","男"),("Female","女"))
    sex = models.CharField(verbose_name = "性别",max_length=4,choices=sex_choice,default='Male')
    professional_title = models.CharField(verbose_name = "职称",max_length=120,default = '大学教师')
    address = models.CharField(verbose_name = "地址",max_length=120,default = '')
    college = models.CharField(verbose_name = "所在大学",max_length=30,default = '')
    academy = models.CharField(verbose_name = "学院",max_length=30,default = '')
    institution = models.CharField(verbose_name = "院系",max_length=30,default = '')
    post_number = models.IntegerField(verbose_name = "邮编号码",default = 0)
    phone_number =  models.CharField(verbose_name = "电话号码",max_length=30,default = '') 
    mail = models.EmailField(verbose_name = "邮箱",max_length = 254)
    content = models.TextField(verbose_name = "简介",default = u'请输入简介')
    UG_lesson = models.TextField(verbose_name = '本科生课程',default='')
    PG_lesson =  models.TextField(verbose_name = '研究生课程',default='')
    research_direction =  models.TextField(verbose_name = '研究方向',default='')
    research =  models.TextField(verbose_name = '科研工作',default='')
    hold_project =  models.TextField(verbose_name = '主持科研项目',default='')
    papers =  models.TextField(verbose_name = '期刊论文',default='')
    books =  models.TextField(verbose_name = '书籍著作',default='')
    conference_papers =  models.TextField(verbose_name = '会议论文',default='')
    recruitment =  models.TextField(verbose_name = '招聘公告',default='')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    def __unicode__(self):
        return self.name	

    def __str__(self):
        return self.name
