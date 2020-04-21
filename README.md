学习Django
====

[![Python Version](https://img.shields.io/badge/python-3.6.5-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-1.11.4-brightgreen.svg)](https://djangoproject.com)

最近在学习Python，看小甲鱼的视频，并参考了[TwoWater](https://github.com/TwoWater)的[草根学Python](https://github.com/TwoWater/Python), 其中提到了Django，和国外一个博客上的Django教程。遂开始学习Django。

**Django教程**: [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)。该教程共包含7个部分（Part）,以搭建一个论坛为例子，较为详细地介绍了Django搭建流程。

在Github上有关于它的中文翻译: [A Complete Beginner's Guide to Django 翻译计划](https://github.com/wzhbingo/django-beginners-guide), 不过目前(2020.04.19)只有前2个Part是完整翻译的，Part3翻译了一部分，剩下的几个部分都还没翻译，该repo也很久未更新，或已中止，所以后面的几个部分只能看英文原版。

学习过程中收获很多, 为防止遗忘，自己动手做一个简略版的记录，也方便以后需要的时候回看。 

**学习进度**
|Part1|Part2|Part3|Part4|Part5|Part6|Part7|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|&radic;|&radic;|&radic;|Learning|||||


# 目录

- [Part1 入门](#part1-入门)
    - [环境搭建](#环境搭建)
    - [Django项目](#django项目)
    - [Django应用](#django应用)
    - [Hello,World](#helloworld)
- [Part2 基础](#part2-基础)
    - [论坛项目](#论坛项目)
    - [Django模型设计](#django模型设计)
    - [迁移模型](#迁移模型)
    - [模型操作](#模型操作)
    - [设置Template](#设置template)
    - [测试主页](#测试主页)
    - [静态文件设置](#静态文件设置)
    - [Django Admin](#django-admin)
- [Part3 进阶](#part3-进阶)
    - [URLs](#urls)
    - [设置Topics页面](#设置topics页面)
    - [测试Topics页面](#测试Topics页面)
    - [添加links](#添加links)
    - [可重用Templates](#可重用templates)
    - [Topbar及其字体](#topbar及其字体)
    - [new\_topic页面](#new-topic页面)
    - [new\_topic表单](#new-topic表单)
    - [Forms API](#form-api)
    - [提交Bootstrap表单](#提交bootstrap表单)
    - [可重用表单模板](#可重用表单模板)
    - [测试表单](#测试表单)
- [Part4 身份验证(Learning)](#part4-身份验证)
    - [创建accounts APP](#创建accounts-app)
    - [注册](#注册)
    - [退出](#退出)
    - [用户菜单](#用户菜单)
    - [登录](#登录)
    - [重置密码](#重置密码)
    - [修改密码](#修改密码)
- [Part5 Django ORM](#part5-djangoorm)
- [Part6 基于类的视图](#part6-基于类的视图)
- [Part7 部署](#part7-部署)

# Part1 入门
[top](#学习Django)

## 环境搭建
* 安装python3
    * 安装方法略，我是之前安装的，版本是3.6.5
* 安装Virtualenv
    * `sudo pip3 install virtualenv`
* 使用virtualenv
    * 新建文件夹myproject : `mkdir myproject`、 `cd myproject`
    * 创建虚拟环境 : `virtualenv venv -p python3`
    * 激活虚拟环境 : `source venv/bin/activate`
    * 退出虚拟环境 : `deactivate`
* 安装Django
    * `pip install django==1.11.4`

## Django项目

* **创建Django项目**: 在myproject文件夹下，开启虚拟环境后，执行下面的命令，创建新的Django项目, 其中`myproject`为项目名称:
    * `django-admin startproject myproject`

* **查看目录结构**: 创建项目成功后，可以使用命令`tree myproject`查看myproject的目录结构，其中的主要文件如下:
    * manage.py
    * \_\_init\_\_.py
    * settings.py
    * urls.py
    * wsgi.py

* **开启服务器**: 在manage.py所在文件夹下，执行下面的命令，开启网络服务器:
    * `python manage.py runserver`

## Django应用

* 在Django项目中，有两个重要的概念：
    * **app**: 完成某个任务的web应用程序, app由models（数据库表）, views（视图）, templates（模板）, tests（测试）组成。
    * **project**: 是配置和应用的集合, 一个项目由一个或多个应用组成。

* **创建Django应用**: 在manage.py所在文件夹执行以下命令,其中`boards`为app名称
    * `django-admin startapp boards`
* **文件解释**: 创建boards应用后，会生成一个以boards为名的文件夹，其中的主要文件（夹）如下：
    * **migrations/**: 存储一些文件，以跟踪models.py文件的变更，用来保持数据库和models.py的同步
    * **admin.py**: Django admin配置文件
    * **apps.py**: 本应用的配置文件
    * **models.py**: 定义web应用数据实例
    * **tests.py**: 单元测试
    * **views.py**: 处理web应用程序请求响应周期的文件

* **启用boards应用**
    * 找到settings.py的`INSTALLED_APPS`列表, 将应用`'boards'`添加到该列表中。

## Hello,World

在views.py和urls.py中添加如下代码:

**views.py**
```python
#在views.py里面添加home函数
from django.http import HttpResponse#new
def home(request):#new
    return HttpResponse('Hello, World!')#new
```

**urls.py**
```python
#在urls.py里面添加匹配url的正则表达式
from django.conf.urls import url
from django.contrib import admin

from boards import views #new

urlpatterns = [
    url(r'^$', views.home, name='home'),#new
    url(r'^admin/', admin.site.urls),
]
```

执行命令`python manage.py runserver`，在浏览器打开[http://127.0.0.1:8000](http://127.0.0.1:8000)，可以看到效果啦

# Part2 基础

[top](#学习Django)

## 论坛项目
项目是一个论坛系统，由多个板块(Boards)组成, 板块由主题帖(Topic)组成，主题帖里有回复帖(Post)，主题帖和回复帖均由用户(User)创建。

所以这个项目共包含四个类Board, Topic, Post, User。由于Django在contrib中内置了User类，所以只需创建其余三个类。

以下两方面需要考虑：

* **各类之间的关系**: 
    * Board and Topic: 1-0..\*
    * Topic and Post: 1-1..\*
    * Topic and User: 0..\*-1
    * Post and User: 0..\*-1
* **各类（模型）的设计**: 
    * Board: 包含两个字段：name和description
    * Topic: 包括四个字段：subject，last\_update，starter, board
    * Post: 有一个message字段，用于存储回复内容，create\_at，update\_at

## Django模型设计

Board, Topic, Post这些模型的设计对应着应用程序的数据库设计。

根据上面的模型设计，相关代码实现在boards/models.py文件中。
```python
from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts')
    updated_by = models.ForeignKey(User, null=True, related_name='+')
```

上面所有模型都是django.db.models.Model类的子类，每个类都将被转换成数据库表。

## 迁移模型

迁移模型就是告诉Django创建数据库，分两步

第一步，执行`python manage.py makemigrations`，执行完产生一个0000\_initial.py文件，该文件代表了应用的当前状态，相当于做了一个汇总，为接下来转换数据库做准备。

第二步，执行`python manage.py migrate`，这一步根据迁移文件生成数据库。

## 模型操作

建好模型，就可以对它进行操作了。

操作之前，要先启动Python shell:

`python manage.py shell`

对模型进行操作的方法总结如下:

|操作|代码示例|
|-|-|
|创建一个对象而不保存|board = Board()|
|保存一个对象|board.save()|
|数据库中创建并保存一个对象|Board.objects.create(name='..',description='..')|
|列出所有对象|Board.objects.all()|
|通过字段标识获取单个对象|Board.objects.get(id=1)|


## 设置Template

在manage.py所在文件夹下新建templates文件夹，并新建文件home.html

**templates/home.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
  </head>
  <body>
    <h1>Boards</h1>

    {% for board in boards %}
      {{ board.name }} <br>
    {% endfor %}

  </body>
</html>
```

在**settings.py**里找到`TEMPLATES`变量，并设置`DIRS`为`os.path.join(BASE_DIR, 'templates')`

然后，修改**boards/views.py**:
```python
from django.shortcuts import render
from .models import Board

def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})
```

## 测试主页

测试环节非常重要。比如测试主页的简单例子:

```python
from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
```
这是一个非常简单但非常有用的测试用例，测试的是请求URL后返回的响应状态码。状态码200意味着成功。当有很多个视图（比如上百个），
用上述测试，只需一个命令，就能够测试是否所有视图返回成功。如果没有自动化测试，我们就需要逐一检查每个页面。

若要查看更详细的信息，可以设置verbosity为2
`python manage.py test --verbosity=2`
`verbosity为0表示无输出，为1表示正常输出，2表示详细输入`

## 静态文件设置

静态文件是指CSS，JavaScript，字体，图片或者用来组成用户界面的任何其他资源

首先在**manage.py**所在文件夹下新建static文件夹.

然后，[下载bootstrap](https://getbootstrap.com/docs/4.0/getting-started/download/#compiled-css-and-js), 解压，将css/bootstrap.min.css放到static文件夹下

修改**templates/home.html**以应用Bootstrap CSS:
```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Boards</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item active">Boards</li>
      </ol>
      <table class="table">
        <thead class="thead-inverse">
          <tr>
            <th>Board</th>
            <th>Posts</th>
            <th>Topics</th>
            <th>Last Post</th>
          </tr>
        </thead>
        <tbody>
          {% for board in boards %}
            <tr>
              <td>
                {{ board.name }}
                <small class="text-muted d-block">{{ board.description }}</small>
              </td>
              <td class="align-middle">0</td>
              <td class="align-middle">0</td>
              <td></td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  </body>
</html>
```

这里原作者的结果图里表头(thead)是黑底白字，但我的不是，也不知道为啥，网上查了查，好像是thead-inverse的作用，
就是不知道为啥thead-inverse在我这里不起作用，后来查了CSS, 发现用下面的语句也可以起到表头黑底白字的作用(强迫症.jpg)：

```html
<style>
    th{
        background-color:black;
        color:white;
    }
</style>
```

## Django Admin

执行`python manage.py createsuperuser`, 依次输入Username, Email, Password即可

启动服务后，访问[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)可以看到登录页面，用刚刚设置的
用户名和密码可以登录, 登录进去以后可以完成一些操作。

# Part3 进阶

[top](#学习Django)

## URLs

Django项目里有一个root URLconf, 在settings.py里面可以找到
`ROOT_URLCONF='myproject.urls'`, 其中`myproject`是项目名称

Django的URL处理流程：
```
request-->urlpatterns-->view function-->html
```

如果在urlpatterns里没有找到匹配的url，就返回404，Page Not Found

url function
```python
def url(regex, view, kwargs=None, name=None):
```

## 设置Topics页面

设置Topics页面需要如下三个步骤：

**首先**，在**url.py**里添加新的URL路由:

**urls.py**
```python
from django.conf.urls import url
from django.contrib import admin

from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),#new
    url(r'^admin/', admin.site.urls),
]
```

**其次**，在views.py里新建board\_topics函数:

**views.py**
```python
from django.shortcuts import render
from .models import Board

def home(request):
    # code suppressed for brevity

def board_topics(request, pk):#new
    board = Board.objects.get(pk=pk)
    return render(request, 'topics.html', {'board': board})
```

**最后**，在templates文件夹，新建topics.html:

**topics.html**
```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{{ board.name }}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        <li class="breadcrumb-item">Boards</li>
        <li class="breadcrumb-item active">{{ board.name }}</li>
      </ol>
    </div>
  </body>
</html>
```

其中, 在urls.py里面添加的语句里面比较重要，尤其是`?P<pk>\d+`

## 测试Topics页面

**boards/tests.py**
```python
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import home, board_topics
from .models import Board

class HomeTests(TestCase):
    # ...

class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
```

用`setUp`创建Board实例来进行测试，因为在执行`python manage.py test`时，Django项目的数据库并没有开启，
也就没办法读取里面的数据，所以测试时必须临时创建，在测试结束时销毁。

## 添加links

前面已经设置了Topics页面，却没有从主页前往Topics页面的links，也没有从Topics页面返回主页的links

添加home--\>Topics's links, 只需修改home.html里面的一行
```html
{{ board.name }}
```
```html
<a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
```

同样的，Topics--\>home, 也只需修改一行
```html
<li class="breadcrumb-item">Boards</li>
```
```html
<li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
```

## 可重用Templates

重构HTML

添加base.html

**templates/base.html**
```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
  </head>
  <body>
    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```

所有的页面均以**base.html**为模板。可以看到**base.html**中有三个block: title, breadcrumb, content。

从效果来看，`breadcrumb`相当于网页路径，类似于访问文件文件夹时的`pwd`。

标题，路径，内容，大概是网页的三个最重要的要素。

然后，以**base.html**为模板修改**home.html**和**topics.html**

**templates/home.html**
```html
{% extends 'base.html' %}

{% block breadcrumb %}
  <li class="breadcrumb-item active">Boards</li>
{% endblock %}

{% block content %}
  <table class="table">
    <thead class="thead-inverse">
      <tr>
        <th>Board</th>
        <th>Posts</th>
        <th>Topics</th>
        <th>Last Post</th>
      </tr>
    </thead>
    <tbody>
      {% for board in boards %}
        <tr>
          <td>
            <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
            <small class="text-muted d-block">{{ board.description }}</small>
          </td>
          <td class="align-middle">0</td>
          <td class="align-middle">0</td>
          <td></td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```
**templates/topics.html**
```html
{% extends 'base.html' %}

{% block title %}
  {{ board.name }} - {{ block.super }}
{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item active">{{ board.name }}</li>
{% endblock %}

{% block content %}
    <!-- just leaving it empty for now. we will add core here soon. -->
{% endblock %}
```

## Topbar及其字体

修改**base.html:**
```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">
  </head>
  <body>

    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
      </div>
    </nav>

    <div class="container">
      <ol class="breadcrumb my-4">
        {% block breadcrumb %}
        {% endblock %}
      </ol>
      {% block content %}
      {% endblock %}
    </div>
  </body>
</html>
```
可以看到, base.html两处作了改动：

* 在`<body>..</body>`里面添加了`<nav>...</nav>`，即Topbar

* 在`<head>..</head>`里面添加了如下两行代码，应用了google的`Peralta`字体
```html
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">
```

此外，还需新建**static/css/app.css**:
```css
.navbar-brand {
  font-family: 'Peralta', cursive;
}
```

## new\_topic页面

修改**urls.py**, 在`urlpatterns`添加:
```python
url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
```

修改**views.py**, 添加`new_topic`函数:
```python
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'new_topic.html', {'board': board})
```
新建**templates/new_topic.html**:
```html
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}

{% endblock %}
```

## new\_topic表单

修改**templates/new_topic.html**
```html
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post">
    {% csrf_token %}
    <div class="form-group">
      <label for="id_subject">Subject</label>
      <input type="text" class="form-control" id="id_subject" name="subject">
    </div>
    <div class="form-group">
      <label for="id_message">Message</label>
      <textarea class="form-control" id="id_message" name="message" rows="5"></textarea>
    </div>
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

## Forms API

使用Forms API

新建**boards/forms.py**:
```python
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Topic
        fields = ['subject', 'message']
```

修改**boards/views.py**中的`new_topic`函数：
```python
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NewTopicForm
from .models import Board, Topic, Post

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
```

更新**new\_topic.html**：
```html
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post", novalidate>
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

注意`novalidate`, 提交为空时，会提示`This field is required`

在**forms.py**里添加`extra attributes`和`help_text`:

**forms.py**
```python
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
```

## 提交Bootstrap表单

使用`django-widget-tweaks`

**首先**，安装:
`pip install django-widget-tweaks`

添加到**settings.py**的`INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',

    'boards',
]
```
其次，在**new\_topic.html**文件里应用:
```html
{% extends 'base.html' %}

{% load widget_tweaks %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post" novalidate>
    {% csrf_token %}

    {% for field in form %}
      <div class="form-group">
        {{ field.label_tag }}

        {% render_field field class="form-control" %}

        {% if field.help_text %}
          <small class="form-text text-muted">
            {{ field.help_text }}
          </small>
        {% endif %}
      </div>
    {% endfor %}

    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

此时，你会发现，提交空内容时不会提示`This field is required`，接着用下面几行替换
`{% render_field field class="form-control" %}`来判断输入内容是否有效
```html
      {% if form.is_bound %}
        {% if field.errors %}

          {% render_field field class="form-control is-invalid" %}
          {% for error in field.errors %}
            <div class="invalid-feedback">
              {{ error }}
            </div>
          {% endfor %}

        {% else %}
          {% render_field field class="form-control is-valid" %}
        {% endif %}
      {% else %}
        {% render_field field class="form-control" %}
      {% endif %}
```
此时，输入为空时，不仅提示`This field is required`而且线框会变红, 而输入内容的线程变绿。

也就是说表单有三种提交状态：
* 初始状态，表单为空，并且`is not bound`, 表单线框为初始的颜色
* 无效输入，表单线框为红色
* 有效输入，表单线框为绿色

## 可重用表单模板

在`templates`文件夹下新建文件夹`includes`;

在`includes`文件夹下新建文件**form.html**:

```html
{% load widget_tweaks %}

{% for field in form %}
  <div class="form-group">
    {{ field.label_tag }}

    {% if form.is_bound %}
      {% if field.errors %}
        {% render_field field class="form-control is-invalid" %}
        {% for error in field.errors %}
          <div class="invalid-feedback">
            {{ error }}
          </div>
        {% endfor %}
      {% else %}
        {% render_field field class="form-control is-valid" %}
      {% endif %}
    {% else %}
      {% render_field field class="form-control" %}
    {% endif %}

    {% if field.help_text %}
      <small class="form-text text-muted">
        {{ field.help_text }}
      </small>
    {% endif %}
  </div>
{% endfor %}
```

修改**new\_topic.html**:
```html
{% extends 'base.html' %}

{% block title %}Start a New Topic{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a></li>
  <li class="breadcrumb-item active">New topic</li>
{% endblock %}

{% block content %}
  <form method="post" novalidate>
    {% csrf_token %}
    {% include 'includes/form.html' %}
    <button type="submit" class="btn btn-success">Post</button>
  </form>
{% endblock %}
```

其实，**form.html**就是把关于表单的部分单独存放, 这样项目中其他地方的表单判断均可引用。

## 测试表单

```python
# ... other imports
from .forms import NewTopicForm

class NewTopicTests(TestCase):
    # ... other tests

    def test_contains_form(self):  # <- new test
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        form = response.context.get('form')
        self.assertIsInstance(form, NewTopicForm)

    def test_new_topic_invalid_post_data(self):  # <- updated this one
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)
```

# Part4 身份验证

[top](#学习Django)

这部分介绍用户相关的一些操作, 注册、登录、退出、修改密码等。

## 创建accounts APP

首先，需要创建accounts APP: `django-admin startapp accounts`

并把**accounts** app添加到settings的`INSTALLED_APPS`

## 注册

修改**myproject/urls.py**:
```python
from django.conf.urls import url
from django.contrib import admin

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
```

在**accounts/views.py**里面添加`signup`函数:
```python
from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')
```

新建**templates/signup.html**:
```html
```

## 退出
## 用户菜单
## 登录
## 重置密码
## 修改密码

# Part5 Django ORM

[top](#学习Django)

# Part6 基于类的视图

[top](#学习Django)

# Part7 部署

[top](#学习Django)
