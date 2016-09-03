#-*-coding:utf-8-*-

from django.shortcuts import render,get_object_or_404
from .models import Teacher
from django.utils import timezone
# Create your views here.

def Teacher_list(request):
    today = timezone.now().date()
    #queryset_list = Teacher.objects.active() #.order_by("-timestamp")
    queryset_list = Teacher.objects.all()
    context = {
		"object_list": queryset_list, 
		"today": today,
	}
    return render(request, "Teacher_list.html", context)



def Teacher_detail(request, slug=None):
	instance = get_object_or_404(Teacher, id=1)
	#share_string = quote_plus(instance.content)
	context = {
		"name": instance.name,
		"instance": instance,
	}
	return render(request, "Teacher_detail.html", context)
