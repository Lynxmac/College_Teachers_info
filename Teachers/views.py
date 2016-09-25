#-*-coding:utf-8-*-

from django.shortcuts import render,get_object_or_404, redirect
from .models import Teacher
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostForm

from django.http import HttpResponseRedirect, Http404 

# Create your views here.

def Teacher_create(request):
    #验证是否为登陆用户或管理员
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    
    #获取request POST过来的表单，将其转换为Django表单
    
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 
        instance = form.save(commit=False)    #保存修改，commit=false是确保form不会自动保存数据
        instance.user = request.user    #用户验证
        instance.save()  #保存
        # message success
        messages.success(request, u"创建成功!")
        return HttpResponseRedirect(instance.get_views_url())
    context = {
        "form": form,
    }
    return render(request, "Teacher_form.html", context)


def Teacher_list(request):
    today = timezone.now().date()
    #queryset_list = Teacher.objects.active() #.order_by("-timestamp")
    queryset_list = Teacher.objects.all()
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(name__icontains=query)|
			Q(content__icontains=query)|
			Q(college__icontains=query) |
			Q(academy__icontains=query) 
			).distinct()
    paginator = Paginator(queryset_list, 6) # 每页显示6个结果
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求页数不是一个整数，则直接返回第一页
        queryset = paginator.page(1)
    except EmptyPage:
        # 如果请求页数超出list的最大索引则返回最后一页
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "教师列表",
        "result":"搜索结果",
        "page_request_var": page_request_var, 
        "today": today,
    }
    return render(request, "Teacher_list.html", context)



def Teacher_detail(request, slug=None):
    instance = get_object_or_404(Teacher,slug=slug)
    #share_string = quote_plus(instance.content)
    context = {
        "name": instance.name,
        "instance": instance,
    }
    return render(request, "Teacher_detail.html", context)


def Teacher_update(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Teacher, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>教师更新成功</a> ", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_views_url())

    context = {
        "title": instance.name,
        "instance": instance,
        "form":form,
    }
    return render(request, "Teacher_form.html", context)



def Teacher_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = get_object_or_404(Teacher, slug=slug)
    name = instance.name
    instance.delete()
    messages.success(request, u"删除%s成功"%name)
    return redirect("Teachers:list")
    
def List_with_api(request):
    return render(request,'Teacher_list_with_api.html')
