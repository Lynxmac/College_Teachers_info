#-*-coding:utf-8-*-

from django.conf.urls import url

from .views import (
    Teacher_list,
    Teacher_detail,
    Teacher_create,
    Teacher_update,
    Teacher_delete,
    List_with_api,
    )

urlpatterns = [
    url(r'^$', Teacher_list, name='list'),
    url(r'^create/$', Teacher_create),
    url(r'^List-rest/$', List_with_api),
    url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', Teacher_update),
    url(r'^(?P<slug>[\w-]+)/delete$', Teacher_delete),
]
