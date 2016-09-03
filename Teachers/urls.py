#-*-coding:utf-8-*-

from django.conf.urls import url

from .views import (
    Teacher_list,
    Teacher_detail
    )

urlpatterns = [
    url(r'^$', Teacher_list, name='list'),
    url(r'^detail$', Teacher_detail, name='detail'),
]
