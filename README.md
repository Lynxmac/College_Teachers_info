# College_Teachers_info

### Django7天建站- 练手项目 -大学教师主页管理

### 目录:

[Day1 : 从创建Web Application到后台管理(代码) ](https://github.com/Lynxmac/College_Teachers_info/tree/dbaf5da7e9ce118c9066bafec3c74694cc55f901)

[Day 2:从urls.py到Templates(代码)](https://github.com/Lynxmac/College_Teachers_info/tree/223c21a85e7cc5239326181f7a3acce5ffab5300)

[Day 3: Django处理url(代码)](https://github.com/Lynxmac/College_Teachers_info/tree/e6a3634eb49facd8e90fdabfc1be7a4b38a94ef2)

[Day4：Django处理静态文件(代码)](https://github.com/Lynxmac/College_Teachers_info/tree/2f6045384756e66ecad76fd913ad4d693a76c224)

[Day 5: 自己编写函数进行后台管理(增删改查)(代码)](https://github.com/Lynxmac/College_Teachers_info/tree/8c7fc73af753d2d93557ba12aa9409aa4bc0f91d)

[Day 6:完善前端(完善教师列表与教师主页界面，添加搜索与分页)(代码)](https://github.com/Lynxmac/College_Teachers_info/tree/bdf6b95fae97eb9a9b3e1900e7788ac7934a7aa2)

[Day 7: 初窥Django REST Framework(代码)](https://github.com/Lynxmac/College_Teachers_info/)



-------

#### 使用前
```

git clone git@github.com:Lynxmac/College_Teachers_info.git
cd College_Teachers_info
pip install requirements.txt

```

##### 下载项目可直接运行查看效果

```

./manage.py runserver 0.0.0.0:8000

#注：0.0.0.0监听来自所有地址的请求，若只在服务器本地测试可改为127.0.0.1


#后台管理：
#账号：root 密码：admin123456

#可自己创建：python manage.py createsuperuser


```

-------


### 开始前: 服务器搭建(Nginx+uWSGI+Django)   *非必需

##### 服务器:ubuntu-14.04 python==2.7.6 Django==1.9.8



参考文章：[Django and Nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)


- ### 服务器的工作流程


> the web client <-> the web server（Nginx） <-> the socket(端口8001) <-> uWSGI <-> Python(Django)



- 直接manage.py runserver 的工作流程

> the web client <-> Python(Django)


##### *服务器搭建可跳过，直接进入网站开发,这里只是测试高并发连接的解决方案

--------


### Day1 : 从创建Web Application到后台管理



- #### 跳过服务器搭建需创建项目，建议使用virtualenv

```
virtualenv Django_site
cd Django_site
source bin/activate

pip install Django == 1.9
pip install wheel==0.24.0
pip install Pillow==3.1.0

#创建Django项目
django-admin startproject mysite

```

1. 创建应用
```
python manage.py startapp Teachers

#将应用添加到settings.py,找到INSTALLED_APPS，添加Teachers

```


2. 修改Teachers/models.py(处理数据库数据增删改查),定义数据类型,在分析该教师主页后，将教师的相关信息划分成多个字段，这里部分字段未添加，如头像，别名等等

#### *教师主页参考[中山大学教师主页](http://sdcs.sysu.edu.cn/space/020165/)
```
class Teacher(models.Model):
    name = models.CharField(verbose_name = '姓名' ,max_length=30,default='')
    sex_choice = (("Male","男"),("Female","女"))
    sex = models.CharField(verbose_name = "性别",max_length=10,choices=sex_choice,default='Male')
    professional_title = models.CharField(verbose_name = "职称",max_length=120,default = '大学教师')
    address = models.CharField(verbose_name = "地址",max_length=120,default = '')
    college = models.CharField(verbose_name = "所在大学",max_length=30,default = '')
    academy = models.CharField(verbose_name = "学院",max_length=30,default = '')
    institution = models.CharField(verbose_name = "院系",max_length=30,default = '')
    post_number = models.IntegerField(verbose_name = "邮编号码",default = 0)
    phone_number =  models.CharField(verbose_name = "电话号码",max_length=30,default = '')
    mail = models.EmailField(verbose_name = "邮箱",max_length = 254)
    content = models.TextField(verbose_name = "简介",default = '请输入简介')
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

```
*models的Fields()参数解释：verbose_name为字段别名，max_length为最大长度，default默认填写，其他相关参数可以查看官方文档[Django-19-models-fields](https://docs.djangoproject.com/en/1.9/ref/models/fields/)*


*__unicode__与__str__的作用使返回的name为教师名字，而非Teacher object(在admin后台管理可以试着注销这两段代码并查看效果)*


3. 数据库修改通知

```
python manage.py makemigrations
```

4. 同步修改


```
python manage.py migrate
```

5. 注册数据库

将Teachers数据库注册到Teachers/Admin.py中,这样就可以在后台管理Teachers数据库,后台http://localhost:8000/admin

```
#-*-coding:utf-8-*-
from .models import Teacher


admin.site.register(Teacher)
```
*要进入后台还需要一个管理员账号，我们可以使用python manage.py createsuperuser创建*

6. 自定义后台管理,修改Teacher/Admin.py,注意添加utf-8注释,


```

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
```




![image](http://upload-images.jianshu.io/upload_images/2935583-4ca3262e989bfef4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-------


### Day 2:从urls.py到Templates

![image](http://upload-images.jianshu.io/upload_images/2935583-229193087f1da759.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


  说一下Django从拿到URL请求时是怎么做的，首先会通过urls.py匹配来决定使用哪个函数，urls.py中有不同的匹配pattern，每个url pattern都对应一个函数，而一般每个不同的函数会有对应的TEMPLATE.html,以http://localhost:8000/Teacher/为例(我们假设它的pattern对应的函数是Teacher_ list()),当Django获得这个URL时，就会使用urls.py中每个pattern去匹配这个URL当匹配成功时(注：若在这个pattern下还有一个pattern可以匹配成功的，Django是不会理的，只执行第一个匹配成功的pattern对应的函数)，Django会执行该pattern对应的函数Teacher_list()，Teacher _list()会执行数据库查询，然后把数据打包，在函数最后的输出可以使用render函数将打包的数据与Template.html渲染为最终响应的response.html。
  讲到这里大概也能理解Django的工作流程，Django其实就是一个MVC框架，但V开头的Views.py在这里是一个控制器
  (Controller)即业务逻辑层,V是Templates属于视图层，M是models.py属于数据存取层。



1. 修改Teachers/views.py,添加第一个函数

```
from .models import Teacher
from django.utils import timezone

def Teacher_list(request):
    today = timezone.now().date()
    #queryset_list = Teacher.objects.active() #.order_by("-timestamp")
    queryset_list = Teacher.objects.all()
    context = {
                "object_list": queryset_list,
                "today": today,
        }
    return render(request, "Teacher_list.html", context)

```

3.创建Teachers/urls.py，向urls.py添加pattern
```
#-*-coding:utf-8-*-

from django.conf.urls import url

from .views import (
    Teacher_list
    )

urlpatterns = [
    url(r'^$', Teacher_list),
]

```
*为什么在Teachers应用里面创建urls.py而不是直接修改mysite/urls.py，这样做的好处就是在后期维护时比较方便，同时不会容易与其他应用混淆*

2. 只在应用里面创建urls.py是没用的，我们还要告诉Django的主urls.py我们这里有一个urls.py，你把它include过去吧，这样应用的urls.py才会生效

修改mysite/urls.py

```
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^Teachers/', include("Teachers.urls")),
]

```
这时Teachers应用的Teacher/urls.py的patterns都在mysite/urls.py里了

*注意：在mysite/urls.py里我们看到Teachers应用的正则匹配式是这样的 r'^Teachers/$'，这也意味着我们要访问Teachers应用的其他页面时，至少需要从http://localhost:8000/Teachers开始*


3. 假如在这个时候我们访问http://localhost:8000/Teachers/，urls.py就会解析到Teacher_list()函数，Teacher_list也会执行其功能，但执行到到return render(request, "Teacher_list.html", context)时，需要一个叫Teacher_list.html的html文件，而这个Teacher_list.html就是我们所说的Template（模板文件）了

##### 什么是Template？

Django的模板有些像php文件，它像一个格式表格，我们可以在这些表格中填写代码或数据。在Django中，Template包含一些特殊的标签，{{var}}可以看作一个变量，在这里我们可以插入指定的数据，{% for obj in objs %}{%endfor%}是一个代码声明，在{{var | linebreaks}} 中的 "|"可看作是Unix的管道符号，linebreaks的功能是不忽略\n换行，更有用的是这个地方的函数可以自己编写，同时Template还有模板继承，引用模板等功能，这些我们后面都会用到。

了解更多可参考这篇文章：

[第四章 模板](http://djangobook.py3k.cn/2.0/chapter04/)

##### 如何使用Template？

首先，需要修改mysite/settings.py，告诉Django templates文件夹在哪，好让Django每次调用模板文件就可以直接在该文件夹下查找了


找到TEMPLATE，将'DIRS':[]修改为
```
'DIRS': [os.path.join(BASE_DIR, 'templates')],
```

在项目根目录下创建templates文件夹

```
mkdir templates
```
在templates下创建Teacher_list.html

```
<!--DOCTYPE html -->

<html>
<body>
<h1>Teacher_list()函数调用了这张模板</h1>

{% for obj in object_list %}

{{obj.name}}</br>

{%endfor%}
<!--这个功能是遍历列表中所有的教师，并显示每位教师的名字，{%for obj in obj_list%}{%endfor%}跟html标签一样闭合的 -->
</body>
</html>

```
重新启动Django服务器，访问http://192.168.1.181:8000/Teachers,返回以下页面

![image](http://upload-images.jianshu.io/upload_images/2935583-50a14378c9cddae1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

*注：我是在局域网测试的，所以访问的是服务器在局域网中的地址，大家如果是在本机测试的话应该访问http://localhost:8000/Teachers或http://127.0.0.1/Teachers*


这时Django基本的工作流程就是这样

> web client ->urls ->views.py(<->models.py<->sqlite) ->templates ->web client


4. 在Teachers/views.py新建函数Teacher_detail()，用于处理教师主页的信息显示


```
from django.shortcuts import get_object_or_404
#get_object_or_404函数功能：按条件查询教师，若教师不存在则返回404页面

def Teacher_detail(request):
	instance = get_object_or_404(Teacher, id=1)
	#share_string = quote_plus(instance.content)
	context = {
		"name": instance.name,
		"instance": instance,
	}
	return render(request, "Teacher_detail.html", context)
```
*注：这里直接将查询id为1的教师信息，也就是我们前面创建的第一个教师*

5.在templates新建Teacher_detail.html，添加以下代码

```
<!--DOCTYPE html -->

<html>
<body>
<h1>Teacher_detail()函数调用了这张模板</h1>

<h1><a>教师简介：</a></h1><hr/>
        <p> ID : {{instance.id}}</p>
        <p>学校：{{instance.college}}</p>
        <p>学院：{{instance.academy}}</p>
        <p>院系：{{instance.institution}}</p>
        <p>职称：{{instance.professional_title}}</p>
        <p>地址：{{instance.address}}</p>
        <p>邮编：{{instance.post_number}}</p>
        <p>邮箱：{{instance.mail}}</p>
        <p>电话：{{instance.phone_number}}</p>

</body>
</html>

```
6 添加pattern到Teachers/urls.py


```
url(r'^detail$', Teacher_detail,),

```
重新启动Django服务器，访问http://192.168.1.181:8000/Teachers/detail,返回以下页面

![image](http://upload-images.jianshu.io/upload_images/2935583-19c2c5b59bad56c7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-------

### Day 3: Django处理url

#### 1.动态URL

我们先来看一下这个pattern
```
url(r'^(?P<id>\d+)/$', Teacher_detail),
```

在打开一个url访问动态网站时，url链接中一般会包含一个或多个相关参数，服务器会根据这些参数来返回不同的数据或不同的页面，Django的urls处理利用正则匹配来获取相关参数，举个简单的例子,下面的匹配pattern ，r'^(?P<id>\d+)/$其中id是作为关键字参数，这样的话假设我们访问了http://localhost:8000/Teachers/?id=1,在匹配这个pattern之后1就会作为数值赋予id，而id则作为关键字参数传递给Teacher_detail

那么我们如何使用这一特性呢？

1. 首先就是将原来匹配Teacher_detail视图的pattern修改为
```
url(r'^(?P<id>\d+)/$', Teacher_detail),
```


2. 修改Teachers/views.py，添加一个传入参数


```
def Teacher_detail(request, id=None):
        instance = get_object_or_404(Teacher, id=id)
        #只需修改这两个位置
```

重新运行Django服务器，访问http://192.168.1.181:8000/Teacher/1/，返回以下画面，

![image](http://upload-images.jianshu.io/upload_images/2935583-38a942f7ddf9fa51.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


2.接下来就是反向解析urls.py里面的pattern来获取一个指定视图的url,pattern里面的name作用就在这了


修改Teachers/urls.py中Teacher_detail的pattern

```
url(r'^(?P<id>\d+)/$', Teacher_detail,name='detail'),
```
*你可能会好奇pattern里面的name是做什么的，假设Teacher_list视图需要是Teacher_detail视图的URL,我们可以在Teacher_list.html使用{% url Teachers:detail %},而在代码中则可以使用reverse(Teachers:detail)*

修改Teachers/models.py，import reverse函数，在类Teacher末尾添加以下功能函数

```
from django.core.urlresolvers import reverse

class Teacher(models.Model):
    ...
    def get_views_url(self):
        return reverse("Teachers:detail",kwargs={"id":self.id})

```

在mysite/urls.py添加为应用Teachers命名空间
```
    url(r'^Teachers/', include("Teachers.urls",namespace='Teachers')),

```

有两种方法可以获取指定教师的URL，第一种在templates/Teacher_list.html调用get_views_url(),第二种方法是用pattern的name来反向获取教师主页的URL，其实两种方法都大同小异
```
<!--DOCTYPE html -->
<html>
...
<a href = "{{obj.get_views_url}}">{{obj.name}}</a></br>

<a href = "{% url "Teachers:detail" id=obj.id %}">{{obj.name}}</a>
...

</html>

```

![image](http://upload-images.jianshu.io/upload_images/2935583-ae1568da39fab5d4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

其返回的html代码如下

```
<a href="/Teachers/1/">邱道文</a><br>
<a href="/Teachers/1/">邱道文</a>

```

### 2.slugify

slug简单来说就是一个链接别名，一个好的Web应用应该拥有简洁、优雅的URL
，以http://192.168.1.181:8000/Teachers/Qiu-Dao-wen/为例 ,链接中Qiu-Dao-wen就是就是我们要实现的slug

1. 删除项目下的db.sqlite3数据库

修改Teachers/models,添加slug字段到class Teacher()，并在class Teacher()后修改get_views.url()

```
...
class Teacher(models.Model):
    ...
    slug = models.SlugField(verbose_name = "链接别名",unique=True)
    ...

    def get_views_url(self):
        return reverse("Teachers:detail",kwargs={"slug":self.slug})

```

2.添加slug的处理函数,Teachers/models


```
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

···
...

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Teacher.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Teacher)

```
3.保存修改

```
python manage.py makemigrations
python manage.py migrate
```

4.重新创建Django管理员

```
python manage.py createsuperuser
```

5.修改Teacher/urls.py

```
url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
```

6.修改Teachers/views.py，将传入Teacher_detail参数改为slug

```
...

def Teacher_detail(request, slug=None):
	instance = get_object_or_404(Teacher, slug=slug)

	...
...
```

重启Django服务，在后台添加数据
![image](http://upload-images.jianshu.io/upload_images/2935583-56412a9e650c00c8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


访问http://192.168.1.181:8000/Teachers/Qiu-Dao-wen/，返回以下画面

![image](http://upload-images.jianshu.io/upload_images/2935583-7b3d49f89954a789.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


-------

### Day4：Django处理静态文件

一个网站通常要能提供其他文件如图片，JS，CSS,。Django 提供静态资源处理的设置，我们可以通过对django.contrib.staticfiles来管理这些静态文件

#### 建立本地存放CSS,JS的static文件夹
*为什么不存放Image呢，因为我们要另外创建一个media专门用来存放媒体文件*
1. 在project/project/settings.py的STATIC_URL下面添加静态文件的保存路径
```
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
#STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")

```

2. 修改project/project/urls.py，
```
from django.conf import settings

#在py文件最后添加以下代码
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


```

3. 保存修改
```

python manage.py collecstatic

```
4. 创建project/static/css/base.css
```
h1 {
    color: #777777;
}

```
5. 在template/Teacher_list.html第一行添加以下代码
```
{% load staticfiles %}

```
6. 向template/Teacher.html的<head>添加以下代码

```

<link rel='stylesheet' href='{% static "css/base.css" %}' />

```

7.可刷新页面查看一级标题是否变为灰色


8.成功后我们会尝试将bootstrap3下载本地，作为我们的静态文件使用，当然一般我们会使用CDN，但这里主要为了练习

```
wget https://github.com/twbs/bootstrap/releases/download/v3.3.7/bootstrap-3.3.7-dist.zip

或

wget http://d.bootcss.com/bootstrap-3.3.0-dist.zip

```

下载后将dist文件夹里面的css,js复制到static文件夹中，fonts我们暂时不需要



文件复制完后，我们就要来调用bootstrap了，为了让模板文件更容易管理，我引进了一个继承的概念，创建一个基础的模板html，再通过继承模板，对基础模板提供的代码块进行修改,这跟网站的footer和导航条类似，它们总会出现在每个页面里，我们不可能每个页面都去添加同样的代码

创建templates/base.html
```
{% load staticfiles %}
<!--DOCTYPE html -->
<html>
<head>
<title>{% block head_title %}教师主页{% endblock head_title %}</title>
<!-- Latest compiled and minified CSS -->
<link rel='stylesheet' href='{% static "css/bootstrap.min.css" %}' />
<link rel='stylesheet' href='{% static "css/bootstrap-theme.min.css" %}' />
<!-- Optional theme -->


<link rel='stylesheet' href='{% static "css/base.css" %}' />
<style>
{% block style %}{% endblock style %}
</style>
</head>
<body>
<div class='container'>

{% block content %}{% endblock content %}

</div>
<!-- Latest compiled and minified JavaScript -->
<script src='{% static "js/bootstrap.min.js" %}'></script>
</body>
</html>
```

*注：直接引进代码块{% include "block.html" %}，相当于插入代码，{%extend base.html%}允许我们修改base.html里面的代码块，同时我们也能添加自己添加代码块，关于代码块我们也需要注意添加修改代码时需要在{%block name%}{%endblock name%}添加修改，在block外面的代码是无效是无效的*

修改templates/Teacher_detail.html如下
```
{% extends "base.html" %}

{%block head_title%}{{instance.name}} | 教师主页{%endblock head_title%}

{%block style%}
.col-center-block {
    float: none;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
{%endblock style%}

{% block content %}
<div class='col-sm-6 col-center-block'style="margin:60px auto auto auto">
<h1>{{instance.name}}</h1>
<div class = 'row'>
    <div class = 'col-sm-6'>
        <p>学校：{{instance.college}}</p>
        <p>学院：{{instance.academy}}</p>
        <p>院系：{{instance.institution}}</p>
        <p>职称：{{instance.professional_title}}</p>
    </div>
    <div class = 'col-sm-6'>
        <p>地址：{{instance.address}}</p>
        <p>邮编：{{instance.post_number}}</p>
        <p>邮箱：{{instance.mail}}</p>
        <p>电话：{{instance.phone_number}}</p>
    </div>
</div>
</div>
{%endblock content%}

```

访问测试

![image](http://upload-images.jianshu.io/upload_images/2935583-5938e56d41a7e47e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 图片的上传与存取

1. 使用ImageField()，向Teachers/models.py的class Teacher()添加以下代码
 ```
class Teacher(models.Model):
    #添加图片字段

    image = models.ImageField(verbose_name = "头像",upload_to=upload_location,
            null=True,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(verbose_name = "高度",default=0)
    width_field = models.IntegerField(verbose_name = "宽度",default=0)

    class Meta:
        ordering = ["-timestamp", "-updated"]
```
2. 修改mysite/settings.py添加MEDIA_URL,MEDIA_ROOT
```

MEDIA_URL = "/media_cdn/"
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "mysite/media_cdn")

```
3. 修改mysite/urls.py
```
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#添加此行代码
```


4.修改Teachers/models.py添加upload_location()

```
...

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)


class Teacher(models.Model):
    ...
...

```
5.在项目根目录创建media_cdn文件夹


6. 保存修改
```
python manage.py makemigrations
python manage.py migrate
```



7.重新运行Django服务，若出现以下错误

>ERRORS:
>Teachers.Teacher.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
>HINT: Get Pillow at https://pypi.python.org/pypi/Pillow or run command "pip install Pillow".

可尝试安装python-dev

```
apt-get install python-dev
```

8.在管理后台修改教师个人档案上传图片

9.在template的Teacher_detail.html里面调用显示图片

```
{% if instance.image %}
         <img src='{{ instance.image.url }}' class='img-responsive center-block' />
        {% endif %}


```

访问测试


![image](http://upload-images.jianshu.io/upload_images/2935583-30883ee43090941b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

-------

### Day 5: 自己编写函数进行后台管理(增删改查)

虽然我们完全可以依赖Django强大的后台管理，但我们也希望开发自己管理函数，数据库的操作就是最基本的增删改查，我们接下来就是要实现这几个基本的功能

在开始之前我们得介绍一下Django Form，Django提供的Form可以帮助我们实现较为复杂的web应。它提供多种函数功能，例如我们下面会用到的is_valid()验证表单，save()保存表单数据，{{form.as_p}}载入表单到html等多种函数功能。那么它是如何实现从前端到后端保存数据呢？我们可以跟着添加教师主页来看一下Django Form是如何实现的

#### 添加教师主页

1. 创建Teachers/forms.py，import Teacher这张表，在将Teacher表中的字段添加fields里面,由forms.ModelForm将其表单化。
```
from django import forms


from .models import Teacher

class PostForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            "name",
            "slug",
            "sex",
            "image",
            "height_field",
            "width_field",
            "professional_title",
            "address",
            "college",
            "academy",
            "institution",
            "post_number",
            "phone_number",
            "mail",
            "content",
            "UG_lesson",
            "PG_lesson",
            "research_direction",
            "research",
            "hold_project",
            "papers",
	        "books",
            "conference_papers",
            "recruitment",
        ]

```

2.创建Teacher_form.html，{%csrf_token%}有在表单内，Django就是通过这个令牌来确认用户的

```
{% extends "base.html" %}

{% block content %}
<div class='col-sm-6 col-sm-offset-3'>
<h1>表单</h1>

<form method='POST' action='' enctype='multipart/form-data'>{% csrf_token %}
{{ form.as_p }}
<input type='submit' class='btn btn-default' value='保存' />
</form>
</div>
{% endblock content %}
```

修改Teacher/views.py，添加Teacher_create()函数

```
from django.contrib import messages

from .forms import PostForm

from django.http import HttpResponseRedirect, Http404

def Teacher_create(request):
    #验证是否为登陆用户或管理员
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	#获取request POST过来的表单，将其转换为Django表单

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)    #保存修改，commit=false是确保form不会自动保存数据
		instance.user = request.user	#用户验证
		instance.save()  #保存
		# message success
		messages.success(request, u"创建成功！")
		return HttpResponseRedirect(instance.get_views_url())
	context = {
		"form": form,
	}
	return render(request, "Teacher_form.html", context)
```

- 添加url pattern到Teachers/urls.py，注意一定要放在Teacher_detail()的pattern前面，否则会提示404,不存在该create这个教师，因为如果我们访问http://192.168.1.181:8000/Teachers/create,如果由Teachers_detail先匹配到，那么它会把create当作一个教师的别名去查询，所以这里要注意一下


3.修改后的urls.py如下

```
#-*-coding:utf-8-*-

from django.conf.urls import url

from .views import (
    Teacher_list,
    Teacher_detail,
    Teacher_create,
    )

urlpatterns = [
    url(r'^$', Teacher_list, name='list'),
    url(r'^create/$', Teacher_create),
    url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
]

```
4. 重新运行Django，访问测试*注意：需要已经登录后台才能在前台进行操作*

![image](http://upload-images.jianshu.io/upload_images/2935583-0000013e8830fb21.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

创建成功重定向到我们新建教师的主页

![image](http://upload-images.jianshu.io/upload_images/2935583-10becb5bae77d146.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


创建成功后之后我们需要添加创建成功的消息提醒

5. 新建messages_show.html
```
{% if messages %}
    <div class='messages'>

    <ul class="messages">
    {% for message in messages %}
    <div class = "row">
    <div class='col-sm-6 col-sm-offset-3'>
    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{% if "html_safe" in message.tags %}<h3>{{ message|safe }}</h3>{% else %}<h3>{{ message }}</h3>{% endif %}</li>
    {% endfor %}
    </ul>
    </div>
    </div>
    </div>
{% endif %}


```
6. 修改templates/base.html，将messages_show.html 插入到<body></body>标签里

```
...
...

<body>
{% include "messages_show.html" %}
<div class='container'>
...
...


```

7. 创建测试*注意：需要已经登录后台才能在前台进行操作*

![image](http://upload-images.jianshu.io/upload_images/2935583-505cc55cae60c384.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


####　更新教师主页

其实更新教师主页跟创建教师并没有太大的区别,只是提前将需要更改的教师主页的数据取出来放入表单中显示出来，再由我们修改，修改后的点击保存到数据成功保存的过程更创建教师主页基本是一样的，只是没有新建一个教师，而是更新该教师的信息。

修改Teachers/views.py，添加Teacher_update()，用于更新教师主页
```

def Teacher_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Teacher, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, u"<a href='#'>教师更新成功</a> ", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_views_url())

	context = {
		"title": instance.name,
		"instance": instance,
		"form":form,
	}
	return render(request, "Teacher_form.html", context)

```


修改urls.py,添加pattern，同时import Teacher_update

```
...

from .views import (
    Teacher_list,
    Teacher_detail,
    Teacher_create,
    Teacher_update,
    )

patterns = [
            url(r'^$', Teacher_list, name='list'),
            url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
            url(r'^(?P<slug>[\w-]+)/edit$', Teacher_update),
            ]
```


重新运行Django ,访问测试*注意：需要已经登录后台才能在前台进行操作*

![image](http://upload-images.jianshu.io/upload_images/2935583-c3a7fce26986cb69.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2935583-d2b9b3692b559f01.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![image](http://upload-images.jianshu.io/upload_images/2935583-e98f02a11e1b0b98.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)




#### 删除教师主页


删除主页比较简单，只需使用get_object_or_404()返回的object自带的delete()函数即可实现删除，具体实现方法如下：

1.修改Teachers/views.py，添加Teacher_delete()函数
```

from django.shortcuts import redirect

def Teacher_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Teacher, slug=slug)
	name = instance.name
	instance.delete()
	messages.success(request, u"删除%s成功"%name)
	return redirect("Teachers:list")

```

2.添加urlpattern 到Teachers/urls.py,同时import Teacher_delete

```
...

from .views import (
    Teacher_list,
    Teacher_detail,
    Teacher_create,
    Teacher_update,
    )

patterns = [
            url(r'^$', Teacher_list, name='list'),
            url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
            url(r'^(?P<slug>[\w-]+)/edit$', Teacher_update),
            url(r'^(?P<slug>[\w-]+)/delete$', Teacher_delete),
            ]

```


3.修改templates/Teacher_list.html，前面测试完动态url之后就一直没改


修改Teacher_list.html如下
```
{% extends "base.html" %}
{% block content %}


{% for obj in object_list %}
  <div class="col-sm-4 col-md-4">
    <div class="thumbnail">
        {% if obj.image %}
         <img src='{{ obj.image.url }}' class='img-responsive center-block' />
        <a href = "{{obj.get_views_url}}">{{obj.name}}   {{obj.slug}}</a><hr/>
        {% endif %}
    </div>
  </div>
{%endfor%}
{%endblock content %}

```

访问删除测试*注意：需要已经登录后台才能在前台进行操作*
![image](http://upload-images.jianshu.io/upload_images/2935583-8dc76ceaba567d9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

删除陈教授的主页http://192.168.1.181:8000/Teachers/Chen-Jiao-Shou/delete


![image](http://upload-images.jianshu.io/upload_images/2935583-51b8ff8380e1d938.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



#### 查询我们已经通过Teacher_list()与Teacher_detail()实现了,不过Day 6我们会介绍搜索与分页

-------

### Day 6:完善前端(完善教师列表与教师主页界面，添加搜索与分页)


#### 完善教师列表页

为教师列表页添加导航栏，在templates创建一个list_nav_bar.html，添加以下代码

```
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
  <div class="container">
   </div>


   <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
   <ul class="nav navbar-nav">
   <li class="pull-left"><a href="/Teachers">教师列表</a></li>
   <li>
   <form class="navbar-form navbar-right" role="search" method='GET' action=''>
   <div class="form-group">
   <input type="text" name = 'q' class="form-control" placeholder="搜索教师" value='{{request.GET.q}}'/>
   </div>
         <button type="submit" class="btn btn-default">搜索</button>
      </form>
   </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>


```
*搜索栏先留空，后面会讲*

因为 navbar-fixed-top的会强制将导航栏固定在页面的顶部，它会遮住body一小部分顶部，因此我们需要在static/css/base.css将body的padding-top设为70x，这样可以让body空出70x的位置来留给导航栏了,同时导航栏中的元素没有居中显示，我们需要修改navbar 的navbar-nav与navbar-collapse样式，添加下面CSS代码到static/css/base.css


```

body {
    padding-top: 70px;
    }

.navbar .navbar-nav {
  display: inline-block;
  float: none;
  vertical-align: top;
}

.navbar .navbar-collapse {
  text-align: center;
}

```

将导航栏代码插入到Teacher_list.html中

```
...

{% block content %}
{%include 'list_nav_bar.html'%}

...
{% endblock content %}

```

原来的教师列表显示头像太大，显得十分不协调，因此列表显示方式也需要修改,

```
<div class='col-sm-6 col-sm-offset-3'>

<div class='row'>


{% for obj in object_list %}
  <div class="col-sm-4 col-md-4">
    <div class="thumbnail">
        {% if obj.image %}
         <img src='{{ obj.image.url }}' class='img-responsive center-block' />
        {% endif %}
      <div class="caption">
        <h3><a href='{{ obj.get_views_url }}'>{{ obj.name }}</a></h3>
        <p>{{ obj.content|linebreaks|truncatechars:20 }}</p>
      </div>
    </div>
  </div>
{% cycle "" "" "</div><hr/><div class='row'>" %}
{% endfor %}
</div>

</div>

```
*{{ obj.content|linebreaks|truncatechars:20 }}，trunckcatechars仅截取20个字符其他省略*

在列表页中每个教师div容器图片都是响应式，容易改变容器大小，我们将强制降图片高度设置为180px
修改static/css/base.css,添加以下样式到文件末端


```

.img-responsive, .thumbnail>img, .thumbnail a>img, .carousel-inner>.item>img, .carousel-inner>.item>a>img{
    display: block;
    max-width: 100%;
    height: 180;
}

```

重新启动Django,访问测试
![image](http://upload-images.jianshu.io/upload_images/2935583-4495183bbfd34174.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



#### 添加分页功能


当教师主页数量增加时，我们希望有一个分页来减少加载结果数量，一次加载太多教师可能会对浏览器造成较大的负担，因此分页是个不错的选择，那么，分页函数应该放在哪呢？

自然是Teacher_list()函数啦！
先import需要的包，然后修改views.py/Teacher_list()如下
```
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Teacher_list(request):
    today = timezone.now().date()
    queryset_list = Teacher.objects.all()
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
                "page_request_var": page_request_var,#注意这里
                "today": today,
        }
    return render(request, "Teacher_list.html", context)

```

使用Django自带的分页函数，将queryset_list切割，将queryset_list切割后，需要对每6个结果进行分页，给出指定页数，当客户端发起一个request，并且request中有一个参数为page,例如http://192.168.1.181:8000/Teachers/?page=2,Django就能根据page=2迅速找到制定queryset_list的结果


修改 Teacher_list.html，显示分页


```
...
...
{% cycle "" "" "</div><hr/><div class='row'>" %}
{% endfor %}
</div>


<div class="pagination">
    <span class="step-links">
        {% if object_list.has_previous %}
            <a href="?{{ page_request_var }}={{ object_list.previous_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}">previous</a>
        {% endif %}

        <span class="current">
            Page {{ object_list.number }} of {{ object_list.paginator.num_pages }}.
        </span>

        {% if object_list.has_next %}
            <a href="?{{ page_request_var }}={{ object_list.next_page_number }}{% if request.GET.q %}&q={{ request.GET.q }}{% endif %}">next</a>
        {% endif %}
    </span>
</div>


</div>
{%endblock content%}
```


![image](http://upload-images.jianshu.io/upload_images/2935583-491e294661f21e6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


#### 添加搜索功能

我们在这里实现的搜索功能是一个过滤的功能，我们在Teacher_list()中我们是先执行一个查询所有查询集，queryset_list = Teacher.objects.all()，再使用Django的Q 对象 (django.db.models.Q) 封装一组关键字参数


```
from django.db.models import Q

...
...

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
    #可在教师姓名，简介，所在大学，所在学院搜索
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
                "title": "教师列表",#注意
                "result":"搜索结果",#注意
                "page_request_var": page_request_var,
                "today": today,
        }
    return render(request, "Teacher_list.html", context)
...
...
```


修改templates/Teacher_list.html ，找到div class='row'，修改如以下代码，主要用来做教师列表页与搜索结果页


```
...
...

{%include 'list_nav_bar.html'%}

<div class='col-sm-6 col-sm-offset-3'>

<div class='row'>


{% if request.GET.q %}
         <h2> {{ result }}</h2>
   {%else%}
        <h2> {{ title }}</h2>
{% endif %}<hr/>

...
...

```


搜索测试
![image](http://upload-images.jianshu.io/upload_images/2935583-623c2e1b2723c4f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



#### 完善教师主页

为教师主页添加导航栏

```

<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
   <div class="container-fluid">

   <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
   <ul class="nav navbar-nav">
   <li class="pull-left"><a href="/Teachers">教师列表</a></li>
   <li ><a href="#intrudution">教师简介</a></li>
   <li ><a href="#teaching">教学工作</a></li>
   <li ><a href="#research">科研工作</a></li>
   <li ><a href="#papers">发表论文</a></li>
   <li ><a href="#recruitment">招聘博士后</a></li>

      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
```
将templates/Teacher_detail.html修改为以下代码

```
{% extends "base.html" %}

{%block head_title%}{{instance.name}} | 教师主页{%endblock head_title%}

{%block style%}
.col-center-block {
    float: none;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
{%endblock style%}

{% block content %}

{% include "detail_nav_bar.html" %}
<div class='col-sm-6 col-center-block'style="margin:0px auto auto auto">
    <div class="col-sm-6 col-center-block">
      <div class = 'thumbnail'>
       {% if instance.image %}
       <img src='{{ instance.image.url }}'/>
       {% endif %}
       <h1 align = 'center' >{{ instance.name }}</h1><br/>
    </div>
     </div>

<h1><a name = "intrudution">教师简介：</a></h1><hr/>
<div class = 'row'>
    <div class = 'col-sm-6'>
        <p>学校：{{instance.college}}</p>
        <p>学院：{{instance.academy}}</p>
        <p>院系：{{instance.institution}}</p>
        <p>职称：{{instance.professional_title}}</p>
    </div>
    <div class = 'col-sm-6'>
        <p>地址：{{instance.address}}</p>
        <p>邮编：{{instance.post_number}}</p>
        <p>邮箱：{{instance.mail}}</p>
        <p>电话：{{instance.phone_number}}</p>
    </div>
</div>
<hr/>
<div class='row'>
<div class='col-sm-12'>

{{ instance.content|linebreaks }}

<hr/>
<br/>
<h1><a name = "teaching">教学工作：</a></h1><hr/>
        {% if instance.UG_lesson%}
        <h3>本科生教程：</h3>
        <p>{{instance.UG_lesson|linebreaks}}</p>
        {%endif%}
        {% if instance.PG_lesson%}
        <h3>本科生教程：</h3>
        <p>{{instance.PG_lesson|linebreaks}}</p>
        {%endif%}
        <hr/>

<h1><a name = "research">科研工作：</a></h1><hr/>
        {% if instance.research_direction%}
                <h3>研究方向：</h3>
                <p>{{instance.research_direction|linebreaks}}</p>
        {%endif%}
        {% if instance.research%}
        <h3>研究工作：</h3>
        <p>{{instance.research|linebreaks}}</p>
        {%endif%}
        {% if instance.hold_project%}
        <h3>主持项目：</h3>
        <p>{{instance.hold_project|linebreaks}}</p>
        {%endif%}
<hr/>
<h1><a name = "papers">发表论文：</a></h1><hr/>
        {% if instance.papers%}
                <h3>期刊论文：</h3>
                <p>{{instance.papers|linebreaks}}</p>
        {%endif%}
        {% if instance.books%}
        <h3>书籍著作：</h3>
        <p>{{instance.books|linebreaks}}</p>
        {%endif%}
        {% if instance.conference_papers%}
        <h3>会议论文：</h3>
        <p>{{instance.conference_papers|linebreaks}}</p>
        {%endif%}
<hr/>
<h1><a name = "recruitment">招聘博士后：</a></h1><hr/>
        {% if instance.recruitment%}
        <p>{{instance.recruitment|linebreaks}}</p>
        {%endif%}

<hr/>


</div>
</div>
</div>
{%endblock content%}

```

重启Django，访问测试
![image](http://upload-images.jianshu.io/upload_images/2935583-8191d8fd513f5b8d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


添加前台管理按钮,在接近enblock content附近添加以下代码，if  request.user.is_superuser会判断当前用户是否为管理员，是的话则给予显示，否则不显示
```
...
...

{% if  request.user.is_superuser  %}
<a href="/Teachers/create"><button class="btn btn-primary btn-mini" type="button">添加教师</button></a>
<a href="{{instance.get_views_url}}edit"><button class="btn btn-success btn-mini" type="button">修改教师</button></a>
<a href="{{instance.get_views_url}}delete"><button class="btn btn-danger btn-mini" type="button">删除教师</button></a>
<hr/>
{% endif %}

</div>
</div>
</div>
{%endblock content%}
```
管理员访问测试

![image](http://upload-images.jianshu.io/upload_images/2935583-ce7d335c59b9c759.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

------

### Day 7: 初窥Django REST Framework

这次我们尝试使用Django REST Framework的Serializer对数据进行渲染，主要是将数据结构序列化为其它格式（XML／JSON 等等），我们可以通过Ajax或XMLHttpRequest等方式来访问API获取数据，当然Django REST Framework也提供接口验证等功能，同样iOS，安卓应用也可以通过这些接口来进行数据交互，我们要实现的是使用angularJS来访问API接口获取JSON数据并加载JSON数据到html中


1.安装Django REST Framework

```
pip install djangorestframework

```

2.在Teachers应用创建目录api，添加__init__.py，

创建views.py

```
#-*-coding:utf-8-*-
from rest_framework.generics import ListAPIView

from Teachers.models import Teacher

class TeacherListAPIView(ListAPIView):
    queryset = Teacher.objects.all()

```

创建urls.py

```
#-*-coding:utf-8-*-
from django.conf.urls import url


from .views import(
    TeacherListAPIView
    )

urlpatterns = [
    url(r'^$', TeacherListAPIView.as_view(), name='list'),

]
```

修改mysite/urls.py

```
...
  ...
  url(r'^', include("Teachers.urls", namespace='Teachers')),
  url(r'^api/Teachers/', include("Teachers.api.urls", namespace='Teachers-api')),
 ]
```

添加Django REST Framework到mysite/settings.py的INSTALLED_APP

```
'Teachers',
'rest_framework',
```

创建Teachers/api/serializers.py,用于将数据序列化为JSON数据，使用Django REST Framework的好处就是它的工作过程跟Django Form的工作方式十分相似

```
#-*-coding:utf-8-*-

from rest_framework.serializers import ModelSerializer

from Teachers.models import Teacher


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "name",
            "slug",
            "image",
        ]
```

修改Teachersapi/views.py,使用serializers.py

```
...
...
from .serializers import TeacherSerializer

class TeacherListAPIView(ListAPIView):
      queryset = Teacher.objects.all()
      serializer_class = TeacherSerializer

```

重启Django，访问测试

![image](http://upload-images.jianshu.io/upload_images/2935583-40a4d8312a198224.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)



接下来就是利用angularJS访问这个接口获取JSON数据，再将JSON数据插入到HTML中


我们在Teachers/views.py中新建一个简单的响应函数,用于返回我们的列表页

```
def List_with_api(request):
    return render(request,'Teacher_list_with_api.html')

```

在Teachers/urls.py添加urlpattern，注意一定要写在slug匹配pattern前面，不然List-r
List_with_api永远不会被匹配到
```
from .views import List_with_api

...
urlpatterns = [
    ...
    url(r'^List-rest/$', List_with_api),
    url(r'^(?P<slug>[\w-]+)/$', Teacher_detail, name='detail'),
    ...
]
```
因为要用到angularJS，我们需要在base.html的头部添加js文件

```
<head>
...

<script src="https://code.angularjs.org/1.4.6/angular.min.js"></script>

...

```

在templates文件夹中创建Teacher_list_with_api.html

```
{% extends "base.html" %}



{% block content %}
{%include 'list_nav_bar.html'%}
{% verbatim %}
<div ng-app="myApp" ng-controller="customersCtrl">
   <div ng-repeat = "Teacher in Teachers">

    <div class="col-sm-4 col-md-4">
    <div class="thumbnail">
        <!--{% if obj.image %}-->
         <img ng-src='{{ Teacher.image }}' class='img-responsive center-block' />
        <!--{% endif %}-->
      <div class="caption">
        <h3><a ng-href='{{ Teacher.slug }}'>{{ Teacher.name }}</a></h3>
      </div>
    </div>
  </div>

<!--{% cycle "" "" "</div><hr/><div class='row'>" %}-->
</div>
</div>
{% endverbatim %}
<script>
var app = angular.module('myApp', []);
app.controller('customersCtrl', function($scope, $http) {
    $http.get("/api/Teachers/?format=json")
    .success(function(response) {
         $scope.Teachers = response
     });
//    $http.get("/api/Teachers/Ji-Xian-Lin/?format=json")
//    .success(function(response) {
//
//         $scope.blog = response;
//
//     });
});
</script>

{%endblock content %}
```
#### *angularJS在HTML中使用变量的标签与Django Template变量模板相冲突，可以使用{% verbatim %}{% endverbatim %}来逃逸Django的渲染*

修改list_nav_bar.html,添加REST-教师列表到导航栏
```
...
   ...

   <li class="pull-left"><a href="/Teachers">教师列表</a></li>
   <li class="pull-left"><a href="/Teachers/List-rest">REST-教师列表</a></li>
   ...
...
```

重启Django,访问测试(/Teachers/Rest-list)

![image](http://upload-images.jianshu.io/upload_images/2935583-d4e335921c127cf9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


使用RESTful API的好处是可以使前端和后端解耦，在实际的生产环境中这样做的好处可以是我们专注在自己擅长的的业务上，在任务上的调配相对清晰，在生产模式上实现多个平台产品兼容，在角色定位上也相对准确，这可以使开发流程更加规范，但开发成本有可能会有所提升

-------

### 感谢：

#### 感谢你能看完这篇又臭又长的教程，希望你能学到有用东西，如果有什么问题可以在项目下开一个issue，我们讨论一下，当然你也可以直接发邮箱给我

#### clynxmac#yahoo.com







