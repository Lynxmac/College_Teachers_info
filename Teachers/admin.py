#-*-coding:utf-8-*-

from django.contrib import admin
from .models import Teacher
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
        list_display = ["name", "updated", "timestamp"]
        #list_display列表显示数据，以此为例，显示标题，
    #更新日期，时间戳
        list_display_links = ["updated"]
        #修改文章详细链接放在更新时间信息上
        list_editable = ["name"]
        #可编辑
        list_filter = ["updated", "timestamp"]
        #过滤盒
        search_fields = ["name", "content"]
        #搜索位置，标题与内容
        class Meta:
                model = Teacher

admin.site.register(Teacher, PostModelAdmin)
