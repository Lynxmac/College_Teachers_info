#-*-coding:utf-8-*-

from django.conf.urls import url

from .views import (
    TeacherListAPIView
    )

urlpatterns = [
    url(r'^$', TeacherListAPIView.as_view(), name='list'),
    
    #url(r'^create/$', Teacher_create),
    #url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
    #url(r'^(?P<slug>[\w-]+)/edit$', Teacher_update),
    #url(r'^(?P<slug>[\w-]+)/delete$', Teacher_delete),
]

