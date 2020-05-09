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
|&radic;|&radic;|&radic;|&radic;|&radic;|Learning||


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
    - [添加背景](#添加背景)
    - [退出](#退出)
    - [显示用户下拉菜单](#显示用户下拉菜单)
    - [登录](#登录)
    - [创建Templates Tags](#创建templates-tags)
    - [重置密码](#重置密码)
    - [修改密码](#修改密码)
- [Part5 Django ORM](#part5-djangoorm)
    - [保护视图](#保护视图)
    - [用户认证](#用户认证)
    - [主题帖视图](#主题帖视图)
    - [回复帖视图](#回复帖视图)
    - [查询集](#查询集)
        - [主页的主题帖数、帖子数、最新回复](#主页的主题帖数帖子数最新回复)
        - [主题帖的回帖数](#主题帖的回帖数)
        - [主题帖的浏览数](#主题帖的浏览数)
- [Part6 基于类的视图](#part6-基于类的视图)
    - [视图策略](#视图策略)
    - [更新视图](#更新视图)
    - [视图列表(分页)](#视图列表分页)
    - [我的账户视图](#我的账户视图)
    - [支持markdown](#支持markdown)
    - [人性化设置](#人性化设置)
    - [头像](#头像)
    - [最后调整](#最后调整)
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
{% extends 'base.html' %}

{% block content %}
  <h2>Sign up</h2>
{% endblock %}
```

对于用户相关操作（sign up, log in password reset），不需要`top bar`，
因此要修改**templates/base.html**, 将`top bar`放到`{block body}`里面，同时，添加一个
`block stylesheet`用于添加CSS代码
```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">
    {% block stylesheet %}{% endblock %}  <!-- HERE -->
  </head>
  <body>
    {% block body %}  <!-- HERE -->
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
    {% endblock body %}  <!-- AND HERE -->
  </body>
</html>
```

在**signup.html**里使用Django自带的`UserCreationForm`:
```html
{% extends 'base.html' %}

{% block body %}
  <div class="container">
    <h2>Sign up</h2>
    <form method="post" novalidate>
      {% csrf_token %}
      {{ form.as_p }}
      <button type="submit" class="btn btn-primary">Create an account</button>
    </form>
  </div>
{% endblock %}
```

在**signup.html**里引用`includes/form.html`:
```html
{% extends 'base.html' %}

{% block body %}
  <div class="container">
    <h2>Sign up</h2>
    <form method="post" novalidate>
      {% csrf_token %}
      {% include 'includes/form.html' %}
      <button type="submit" class="btn btn-primary">Create an account</button>
    </form>
  </div>
{% endblock %}
```

此时，会出现一些乱码，有必要修改一下**includes/form.html**:
```html
{% load widget_tweaks %}

{% for field in form %}
  <div class="form-group">
    {{ field.label_tag }}

    <!-- code suppressed for brevity -->

    {% if field.help_text %}
      <small class="form-text text-muted">
        {{ field.help_text|safe }}  <!-- new code here -->
      </small>
    {% endif %}
  </div>
{% endfor %}
```

进一步修改**accounts/views.py**:
```python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
```

接着，把用户名添加到`top bar`, 需要修改**templates/base.html**的`top bar`部分:
```html
{% block body %}
  <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
    <div class="container">
      <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#mainMenu" aria-controls="mainMenu" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="mainMenu">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="#">{{ user.username }}</a>
          </li>
        </ul>
      </div>
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
{% endblock body %}
```

前面的注册表单里面没有邮件这一项，因为UserCreationForm里面没有提供。所以我们需要自己来对它进行扩展。

创建**accounts/forms.py**:
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
```

然后，在**accounts/views.py**里面就直接用`SignUpForm`来代替`UserCreationForm`了
```python
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
```

## 添加背景

* 首先在`static`文件夹下新建一个文件夹img.
* 然后，在[https://www.toptal.com/designers/subtlepatterns/](https://www.toptal.com/designers/subtlepatterns/)下载一个背景图片，并放到static/img/目录下
* 在static/css文件夹新建accounts.css：
```css
body {
  background-image: url(../img/shattered.png);
}

.logo {
  font-family: 'Peralta', cursive;
}

.logo a {
  color: rgba(0,0,0,.9);
}

.logo a:hover,
.logo a:active {
  text-decoration: none;
}
```
* 接着，修改templates/signup.html，应用accounts.css:
```html
{% extends 'base.html' %}

{% load static %}

{% block stylesheet %}
  <link rel="stylesheet" href="{% static 'css/accounts.css' %}">
{% endblock %}

{% block body %}
  <div class="container">
    <h1 class="text-center logo my-4">
      <a href="{% url 'home' %}">Django Boards</a>
    </h1>
    <div class="row justify-content-center">
      <div class="col-lg-8 col-md-10 col-sm-12">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Sign up</h3>
            <form method="post" novalidate>
              {% csrf_token %}
              {% include 'includes/form.html' %}
              <button type="submit" class="btn btn-primary btn-block">Create an account</button>
            </form>
          </div>
          <div class="card-footer text-muted text-center">
            Already have an account? <a href="#">Log in</a>
          </div>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
```

## 退出

* 修改**urls.py**,添加路由：
```python
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
```

* 设置**settings.py**,添加`LOGOUT_REDIRECT_URL`变量:
```python
LOGOUT_REDIRECT_URL = 'home'
```
这样，退出以后，跳转到主页

## 显示用户下拉菜单

设置用户下拉菜单栏需要下载几个依赖文件：
* jquery-x.x.x.min.js, 其中x.x.x是版本号, 下载地址: [https://jquery.com/download/](https://jquery.com/download/), 下载**compressed,production jQuery**最新版即可，我下的版本是3.5.0，下载时直接出来了内容页面，复制它们，保存在jquery-3.5.0.min.js，即可
* popper.min.js, 下载地址: [https://popper.js.org/](https://popper.js.org/)，官网好像没有源码下载了，我是用npm下载的, 执行`npm i @popperjs/core`, 然后在`node_models/@popperjs/core/dist/umd`文件夹下找到`popper.min.js`。
* bootstrap.min.js, 下载地址：[https://getbootstrap.com/](https://getbootstrap.com/)

在文件夹**static**下新建文件夹**js**,将上面三个js文件放到该文件夹下。

然后，修改**base.html**:
```html
{% load static %}<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>{% block title %}Django Boards{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css?family=Peralta" rel="stylesheet">
    <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/app.css' %}">
    {% block stylesheet %}{% endblock %}
  </head>
  <body>
    {% block body %}
    <!-- code suppressed for brevity -->
    {% endblock body %}
    <script src="{% static 'js/jquery-3.2.1.min.js' %}"></script>
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
  </body>
</html>
```

修改**base.html**的<nav>...</nav>部分, 设置下拉菜单,并对用户是否登录进行判断:
```html
<nav class="navbar navbar-expand-sm navbar-dark bg-dark">
  <div class="container">
    <a class="navbar-brand" href="{% url 'home' %}">Django Boards</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#mainMenu" aria-controls="mainMenu" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="mainMenu">
      {% if user.is_authenticated %} <!--判断用户是否登录-->
        <ul class="navbar-nav ml-auto"> 
          <li class="nav-item dropdown"> <!--下拉菜单-->
            <a class="nav-link dropdown-toggle" href="#" id="userMenu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              {{ user.username }}
            </a>
            <div class="dropdown-menu dropdown-menu-right" aria-labelledby="userMenu">
              <a class="dropdown-item" href="#">My account</a>
              <a class="dropdown-item" href="#">Change password</a>
              <div class="dropdown-divider"></div>
              <a class="dropdown-item" href="{% url 'logout' %}">Log out</a>
            </div>
          </li> <!--下拉菜单-->
        </ul>
      {% else %}
        <form class="form-inline ml-auto">
          <a href="#" class="btn btn-outline-secondary">Log in</a>
          <a href="{% url 'signup' %}" class="btn btn-primary ml-2">Sign up</a>
        </form>
      {% endif %}
    </div>
  </div>
</nav>
```

## 登录

* **urls.py**
* **settings.py**
* **base.html**
* **login.html**

**urls.py**
```python
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    url(r'^admin/', admin.site.urls),
]
```
**settings.py**
```python
LOGIN_REDIRECT_URL = 'home'
```
**base.html**
```html
<a href="{% url 'login' %}" class="btn btn-outline-secondary">Log in</a>
```
**login.html**
```html
{% extends 'base.html' %}

{% load static %}

{% block stylesheet %}
  <link rel="stylesheet" href="{% static 'css/accounts.css' %}">
{% endblock %}

{% block body %}
  <div class="container">
    <h1 class="text-center logo my-4">
      <a href="{% url 'home' %}">Django Boards</a>
    </h1>
    <div class="row justify-content-center">
      <div class="col-lg-4 col-md-6 col-sm-8">
        <div class="card">
          <div class="card-body">
            <h3 class="card-title">Log in</h3>
            <form method="post" novalidate>
              {% csrf_token %}
              {% include 'includes/form.html' %}
              <button type="submit" class="btn btn-primary btn-block">Log in</button>
            </form>
          </div>
          <div class="card-footer text-muted text-center">
            New to Django Boards? <a href="{% url 'signup' %}">Sign up</a>
          </div>
        </div>
        <div class="text-center py-2">
          <small>
            <a href="#" class="text-muted">Forgot your password?</a>
          </small>
        </div>
      </div>
    </div>
  </div>
{% endblock %}
```

接着，考虑重构一些用户操作相关的HTML, 新建**base_accounts.html**文件
```html
{% extends 'base.html' %}

{% load static %}

{% block stylesheet %}
  <link rel="stylesheet" href="{% static 'css/accounts.css' %}">
{% endblock %}

{% block body %}
  <div class="container">
    <h1 class="text-center logo my-4">
      <a href="{% url 'home' %}">Django Boards</a>
    </h1>
    {% block content %}
    {% endblock %}
  </div>
{% endblock %}
```
并应用到**signup.html**和**login.html**

**判断用户名是否存在**,在**includes/form.html**添加：
```html
{% load widget_tweaks %}

{% if form.non_field_errors %}
  <div class="alert alert-danger" role="alert">
    {% for error in form.non_field_errors %}
      <p{% if forloop.last %} class="mb-0"{% endif %}>{{ error }}</p>
    {% endfor %}
  </div>
{% endif %}

{% for field in form %}
  <!-- code suppressed -->
{% endfor %}
```

## 创建Templates Tags

在boards文件夹下新建templatetags文件夹，并新建`__init__.py`和`form_tags.py`两个文件

**form_tags.py**
```python
from django import template

register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)
```

然后更新**includes/form.html**
```html
{% load form_tags widget_tweaks %}

{% if form.non_field_errors %}
  <div class="alert alert-danger" role="alert">
    {% for error in form.non_field_errors %}
      <p{% if forloop.last %} class="mb-0"{% endif %}>{{ error }}</p>
    {% endfor %}
  </div>
{% endif %}

{% for field in form %}
  <div class="form-group">
    {{ field.label_tag }}
    {% render_field field class=field|input_class %}
    {% for error in field.errors %}
      <div class="invalid-feedback">
        {{ error }}
      </div>
    {% endfor %}
    {% if field.help_text %}
      <small class="form-text text-muted">
        {{ field.help_text|safe }}
      </small>
    {% endif %}
  </div>
{% endfor %}
```

## 重置密码

重置密码涉及到较多的URLs, 另外重置密码前需要先发送邮件，重置密码的URL放在邮件里

* **myproject/settings.py**, 添加`EMAIL_BACKEND`变量
```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```
* urls.py
```python
url(r'^reset/$',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html',
        email_template_name='password_reset_email.html',
        subject_template_name='password_reset_subject.txt'
    ),
    name='password_reset'),
url(r'^reset/done/$',
    auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
    name='password_reset_done'),
url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
    name='password_reset_confirm'),
url(r'^reset/complete/$',
    auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
    name='password_reset_complete'),
]
```
* templates/
    * password_reset.html
    ```html
    {% extends 'base_accounts.html' %}
    
    {% block title %}Reset your password{% endblock %}
    
    {% block content %}
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-8">
          <div class="card">
            <div class="card-body">
              <h3 class="card-title">Reset your password</h3>
              <p>Enter your email address and we will send you a link to reset your password.</p>
              <form method="post" novalidate>
                {% csrf_token %}
                {% include 'includes/form.html' %}
                <button type="submit" class="btn btn-primary btn-block">Send password reset email</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    {% endblock %}
    ```
    * password_reset_subject.txt
    ```txt
    [Django Boards] Please reset your password
    ```
    * password_reset_email.html
    ```html
    Hi there,

    Someone asked for a password reset for the email address {{ email }}.
    Follow the link below:
    {{ protocol }}://{{ domain }}{% url 'password_reset_confirm' uidb64=uid token=token %}
    
    In case you forgot your Django Boards username: {{ user.username }}
    
    If clicking the link above doesn't work, please copy and paste the URL
    in a new browser window instead.
    
    If you've received this mail in error, it's likely that another user entered
    your email address by mistake while trying to reset a password. If you didn't
    initiate the request, you don't need to take any further action and can safely
    disregard this email.
    
    Thanks,
    
    The Django Boards Team
    ```
    * password_reset_done.html
    ```html
    {% extends 'base_accounts.html' %}

    {% block title %}Reset your password{% endblock %}
    
    {% block content %}
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-8">
          <div class="card">
            <div class="card-body">
              <h3 class="card-title">Reset your password</h3>
              <p>Check your email for a link to reset your password. If it doesn't appear within a few minutes, check your spam folder.</p>
              <a href="{% url 'login' %}" class="btn btn-secondary btn-block">Return to log in</a>
            </div>
          </div>
        </div>
      </div>
    {% endblock %}
    ```
    * password_reset_confirm.html
    ```html
    {% extends 'base_accounts.html' %}
    
    {% block title %}
      {% if validlink %}
        Change password for {{ form.user.username }}
      {% else %}
        Reset your password
      {% endif %}
    {% endblock %}
    
    {% block content %}
      <div class="row justify-content-center">
        <div class="col-lg-6 col-md-8 col-sm-10">
          <div class="card">
            <div class="card-body">
              {% if validlink %}
                <h3 class="card-title">Change password for @{{ form.user.username }}</h3>
                <form method="post" novalidate>
                  {% csrf_token %}
                  {% include 'includes/form.html' %}
                  <button type="submit" class="btn btn-success btn-block">Change password</button>
                </form>
              {% else %}
                <h3 class="card-title">Reset your password</h3>
                <div class="alert alert-danger" role="alert">
                  It looks like you clicked on an invalid password reset link. Please try again.
                </div>
                <a href="{% url 'password_reset' %}" class="btn btn-secondary btn-block">Request a new password reset link</a>
              {% endif %}
            </div>
          </div>
        </div>
      </div>
    {% endblock %}
    ```
    * password_reset_complete.html
    ```html
    {% extends 'base_accounts.html' %}

    {% block title %}Password changed!{% endblock %}
    
    {% block content %}
      <div class="row justify-content-center">
        <div class="col-lg-6 col-md-8 col-sm-10">
          <div class="card">
            <div class="card-body">
              <h3 class="card-title">Password changed!</h3>
              <div class="alert alert-success" role="alert">
                You have successfully changed your password! You may now proceed to log in.
              </div>
              <a href="{% url 'login' %}" class="btn btn-secondary btn-block">Return to log in</a>
            </div>
          </div>
        </div>
      </div>
    {% endblock %}
    ```

## 修改密码

* urls.py
```python
url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
```
* settings.py
```python
LOGIN_URL = 'login'
```
* templates/
    * password_change.html
    ```html
    {% extends 'base.html' %}

    {% block title %}Change password{% endblock %}
    
    {% block breadcrumb %}
      <li class="breadcrumb-item active">Change password</li>
    {% endblock %}
    
    {% block content %}
      <div class="row">
        <div class="col-lg-6 col-md-8 col-sm-10">
          <form method="post" novalidate>
            {% csrf_token %}
            {% include 'includes/form.html' %}
            <button type="submit" class="btn btn-success">Change password</button>
          </form>
        </div>
      </div>
    {% endblock %}
    ```
    * password_change_done.html
    ```html
    {% extends 'base.html' %}

    {% block title %}Change password successful{% endblock %}
    
    {% block breadcrumb %}
      <li class="breadcrumb-item"><a href="{% url 'password_change' %}">Change password</a></li>
      <li class="breadcrumb-item active">Success</li>
    {% endblock %}
    
    {% block content %}
      <div class="alert alert-success" role="alert">
        <strong>Success!</strong> Your password has been changed!
      </div>
      <a href="{% url 'home' %}" class="btn btn-secondary">Return to home page</a>
    {% endblock %}
    ```

# Part5 Django ORM

[top](#学习Django)

## 保护视图

对于`new_topic.html`这类页面，必须用户登录才能进去, 如果没登录就跳转到登录页面:

Django提供了这个功能，只需要在**views.py**里的`new_topic`函数前面加上`@login_required`

登录之后，还需要重定向到原来的页面。修改**templates/login.html**:
```html
<form method="post" novalidate>
  {% csrf_token %}
  <input type="hidden" name="next" value="{{ next }}">
  {% include 'includes/form.html' %}
  <button type="submit" class="btn btn-primary btn-block">Log in</button>
</form>
```

## 用户认证

**boards/views.py**
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewTopicForm
from .models import Board, Post

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user  # <- here
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=request.user  # <- and here
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})
```

## 主题帖视图

* urls.py
`url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.topic_posts, name='topic_posts'),`
* boards/views.py
```python
from django.shortcuts import get_object_or_404, render
from .models import Topic

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    return render(request, 'topic_posts.html', {'topic': topic})
```
* `templates/topic_posts.html`
```python
{% extends 'base.html' %}

{% load static %}

{% block title %}{{ topic.subject }}{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' topic.board.pk %}">{{ topic.board.name }}</a></li>
  <li class="breadcrumb-item active">{{ topic.subject }}</li>
{% endblock %}

{% block content %}

  <div class="mb-4">
    <a href="#" class="btn btn-primary" role="button">Reply</a>
  </div>

  {% for post in topic.posts.all %}
    <div class="card mb-2">
      <div class="card-body p-3">
        <div class="row">
          <div class="col-2">
            <img src="{% static 'img/avatar.svg' %}" alt="{{ post.created_by.username }}" class="w-100">
            <small>Posts: {{ post.created_by.posts.count }}</small>
          </div>
          <div class="col-10">
            <div class="row mb-3">
              <div class="col-6">
                <strong class="text-muted">{{ post.created_by.username }}</strong>
              </div>
              <div class="col-6 text-right">
                <small class="text-muted">{{ post.created_at }}</small>
              </div>
            </div>
            {{ post.message }}
            {% if post.created_by == user %}
              <div class="mt-3">
                <a href="#" class="btn btn-primary btn-sm" role="button">Edit</a>
              </div>
            {% endif %}
          </div>
        </div>
      </div>
    </div>
  {% endfor %}

{% endblock %}
```

## 回复帖视图

* urls.py
`url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$', views.reply_topic, name='reply_topic'),`
* boards/forms.py
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]
```
* boards/views.py
```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm
from .models import Topic

@login_required
def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            # code suppressed ...
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)  # <- here
    # code suppressed ...

@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})

```
* templates/reply_topic.html
```html
{% extends 'base.html' %}

{% load static %}

{% block title %}Post a reply{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' topic.board.pk %}">{{ topic.board.name }}</a></li>
  <li class="breadcrumb-item"><a href="{% url 'topic_posts' topic.board.pk topic.pk %}">{{ topic.subject }}</a></li>
  <li class="breadcrumb-item active">Post a reply</li>
{% endblock %}

{% block content %}

  <form method="post" class="mb-4">
    {% csrf_token %}
    {% include 'includes/form.html' %}
    <button type="submit" class="btn btn-success">Post a reply</button>
  </form>

  {% for post in topic.posts.all %}
    <div class="card mb-2">
      <div class="card-body p-3">
        <div class="row mb-3">
          <div class="col-6">
            <strong class="text-muted">{{ post.created_by.username }}</strong>
          </div>
          <div class="col-6 text-right">
            <small class="text-muted">{{ post.created_at }}</small>
          </div>
        </div>
        {{ post.message }}
      </div>
    </div>
  {% endfor %}

{% endblock %}
```

* **templates/topic_posts.html**:
```html
{% for post in topic.posts.all %}
  <div class="card mb-2 {% if forloop.first %}border-dark{% endif %}">
    {% if forloop.first %}
      <div class="card-header text-white bg-dark py-2 px-3">{{ topic.subject }}</div>
    {% endif %}
    <div class="card-body p-3">
      <!-- code suppressed -->
    </div>
  </div>
{% endfor %}
```

## 查询集

显示主页的主题数、回帖数，以及主题帖的回帖数和浏览数

### 主页的主题帖数、帖子数、最新回复

首先，为所有的models添加`__str__`方法
**boards/models.py**
```python
from django.db import models
from django.utils.text import Truncator

class Board(models.Model):
    # ...
    def __str__(self):
        return self.name

class Topic(models.Model):
    # ...
    def __str__(self):
        return self.subject

class Post(models.Model):
    # ...
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
```

主题数比较简单，可以直接用`board.topics.count()`表示

而帖子数和最新回复需要修改**boards/models.py**
```python
from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_posts_count(self): # <-- new
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):   # <-- new
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()
```
其中，`get_posts_count`返回board的帖子数, `get_last_post`返回board的最新回复

然后，在`templates/home.html`里面的相应位置修改:
`templates/home.html`
```html
    <tbody>
      {% for board in boards %}
        <tr>
          <td>
            <a href="{% url 'board_topics' board.pk %}">{{ board.name }}</a>
            <small class="text-muted d-block">{{ board.description }}</small>
          </td>
          <td class="align-middle">
            {{ board.get_posts_count }}
          </td>
          <td class="align-middle">
            {{ board.topics.count }}
          </td>
          <td class="align-middle">
            {% with post=board.get_last_post %}
              {% if post %}
                <small>
                  <a href="{% url 'topic_posts' board.pk post.topic.pk %}">
                    By {{ post.created_by.username }} at {{ post.created_at }}
                  </a>
                </small>
              {% else %}
                <small class="text-muted">
                  <em>No posts yet.</em>
                </small>
              {% endif %}
            {% endwith %}
          </td>
        </tr>
      {% endfor %}
    </tbody>
```

### 主题帖的回帖数

* 在boards/views.py的`board_topics`函数里添加一行
`topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)`
* 然后修改templates/topics.html
```html
{% for topic in topics %}
  <tr>
    <td><a href="{% url 'topic_posts' board.pk topic.pk %}">{{ topic.subject }}</a></td>
    <td>{{ topic.starter.username }}</td>
    <td>{{ topic.replies }}</td>
    <td>0</td>
    <td>{{ topic.last_updated }}</td>
  </tr>
{% endfor %}
```

### 主题帖的浏览数

显示主题帖的浏览数需要新建views field, 然后需要迁移（也就是将新添加的field更新到数据库）

在boards/models.py文件里添加views field
```python
class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics')
    starter = models.ForeignKey(User, related_name='topics')
    views = models.PositiveIntegerField(default=0)  # <- here

    def __str__(self):
        return self.subject
```
boards/views.py
```python
from django.shortcuts import get_object_or_404, render
from .models import Topic

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})
```
templates/topics.html
```html
{% for topic in topics %}
  <tr>
    <td><a href="{% url 'topic_posts' board.pk topic.pk %}">{{ topic.subject }}</a></td>
    <td>{{ topic.starter.username }}</td>
    <td>{{ topic.replies }}</td>
    <td>{{ topic.views }}</td>  <!-- here -->
    <td>{{ topic.last_updated }}</td>
  </tr>
{% endfor %}
```

# Part6 基于类的视图

[top](#学习Django)

## 视图策略

常用的视图有三种：
* Function-Based Views(FBV)
* Class-Based Views(CBV)
* Generic Class-Based Views(GCBV)

FBV是最简单的视图，通过函数来接受一个`HttpRequest`，然后返回一个`HttpResponse`。

CBV就是把定义视图的函数封装起来，放在一个类里，这个类扩展了`django.views.generic.View`这个抽象类。

GCBV是内置的CBV。

## 更新视图

现在用GCBV来实现编辑帖子（edit post）的视图

修改**boards/views.py**
```python
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.utils import timezone

class PostUpdateView(UpdateView):
    model = Post
    fields = ('message', )
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', pk=post.topic.board.pk, topic_pk=post.topic.pk)
```
**urls.py**
```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    # ...
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        views.PostUpdateView.as_view(), name='edit_post'),
]
```

然后，在`topic_post.html`里添加链接
```html
{% if post.created_by == user %}
  <div class="mt-3">
    <a href="{% url 'edit_post' post.topic.board.pk post.topic.pk post.pk %}"
       class="btn btn-primary btn-sm"
       role="button">Edit</a>
  </div>
{% endif %}
```

`templates/edit_post.html`
```html
{% extends 'base.html' %}

{% block title %}Edit post{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item"><a href="{% url 'home' %}">Boards</a></li>
  <li class="breadcrumb-item"><a href="{% url 'board_topics' post.topic.board.pk %}">{{ post.topic.board.name }}</a></li>
  <li class="breadcrumb-item"><a href="{% url 'topic_posts' post.topic.board.pk post.topic.pk %}">{{ post.topic.subject }}</a></li>
  <li class="breadcrumb-item active">Edit post</li>
{% endblock %}

{% block content %}
  <form method="post" class="mb-4" novalidate>
    {% csrf_token %}
    {% include 'includes/form.html' %}
    <button type="submit" class="btn btn-success">Save changes</button>
    <a href="{% url 'topic_posts' post.topic.board.pk post.topic.pk %}" class="btn btn-outline-secondary" role="button">Cancel</a>
  </form>
{% endblock %}
```

* `login_required`

## 视图列表

采用GCBV视图策略，以`home.html`为例，修改`views.py`和`urls.py`
**views.py**
```python
from django.views.generic import ListView
from .models import Board

class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'home.html'
```
**urls.py**
```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    url(r'^$', views.BoardListView.as_view(), name='home'),
    # ...
]
```

## 分页

当帖子数太多时，就需要进行分页。

分页之前，先添加一些帖子：

* 首先，执行`python manage.py shell`，进入python命令行
* 然后，依次执行以下命令就可以了：
```python
from django.contrib.auth.models import User
from boards.models import Board, Topic, Post

user = User.objects.first()

board = Board.objects.get(name='Django')

for i in range(100):
    subject = 'Topic test #{}'.format(i)
    topic = Topic.objects.create(subject=subject, board=board, starter=user)
    Post.objects.create(message='Lorem ipsum...', topic=topic, created_by=user)
```

### FBV分页

boards/views.py
```python
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Board

def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    queryset = board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
    page = request.GET.get('page', 1)

    paginator = Paginator(queryset, 20)

    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        # fallback to the first page
        topics = paginator.page(1)
    except EmptyPage:
        # probably the user tried to add a page number
        # in the url, so we fallback to the last page
        topics = paginator.page(paginator.num_pages)

    return render(request, 'topics.html', {'board': board, 'topics': topics})
```
templates/topics.html:
```html
{% if topics.has_other_pages %}
  <nav aria-label="Topics pagination" class="mb-4">
    <ul class="pagination">
      {% if topics.has_previous %}
        <li class="page-item">
          <a class="page-link" href="?page={{ topics.previous_page_number }}">Previous</a>
        </li>
      {% else %}
        <li class="page-item disabled">
          <span class="page-link">Previous</span>
        </li>
      {% endif %}

      {% for page_num in topics.paginator.page_range %}
        {% if topics.number == page_num %}
          <li class="page-item active">
            <span class="page-link">
              {{ page_num }}
              <span class="sr-only">(current)</span>
            </span>
          </li>
        {% else %}
          <li class="page-item">
            <a class="page-link" href="?page={{ page_num }}">{{ page_num }}</a>
          </li>
        {% endif %}
      {% endfor %}

      {% if topics.has_next %}
        <li class="page-item">
          <a class="page-link" href="?page={{ topics.next_page_number }}">Next</a>
        </li>
      {% else %}
        <li class="page-item disabled">
          <span class="page-link">Next</span>
        </li>
      {% endif %}
    </ul>
  </nav>
{% endif %}
```

### GCBV分页

boards/views.py
```python
class TopicListView(ListView):
    model = Topic
    context_object_name = 'topics'
    template_name = 'topics.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        kwargs['board'] = self.board
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.board = get_object_or_404(Board, pk=self.kwargs.get('pk'))
        queryset = self.board.topics.order_by('-last_updated').annotate(replies=Count('posts') - 1)
        return queryset
```
urls.py
```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    # ...
    url(r'^boards/(?P<pk>\d+)/$', views.TopicListView.as_view(), name='board_topics'),
]
```

templates/topics.html
```html
{% block content %}
  <div class="mb-4">
    <a href="{% url 'new_topic' board.pk %}" class="btn btn-primary">New topic</a>
  </div>

  <table class="table mb-4">
    <!-- table content suppressed -->
  </table>

  {% if is_paginated %}
    <nav aria-label="Topics pagination" class="mb-4">
      <ul class="pagination">
        {% if page_obj.has_previous %}
          <li class="page-item">
            <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
          </li>
        {% else %}
          <li class="page-item disabled">
            <span class="page-link">Previous</span>
          </li>
        {% endif %}

        {% for page_num in paginator.page_range %}
          {% if page_obj.number == page_num %}
            <li class="page-item active">
              <span class="page-link">
                {{ page_num }}
                <span class="sr-only">(current)</span>
              </span>
            </li>
          {% else %}
            <li class="page-item">
              <a class="page-link" href="?page={{ page_num }}">{{ page_num }}</a>
            </li>
          {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
          <li class="page-item">
            <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
          </li>
        {% else %}
          <li class="page-item disabled">
            <span class="page-link">Next</span>
          </li>
        {% endif %}
      </ul>
    </nav>
  {% endif %}

{% endblock %}
```

## 可重用分页模板

事实上，不光主页需要分页，每个帖子的回复帖多了，也需要分页，所以采用模板实现会方便很多。

boards/views.py
```python
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'topic_posts.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        self.topic.views += 1
        self.topic.save()
        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset
```
urls.py
```python
from django.conf.urls import url
from boards import views

urlpatterns = [
    # ...
    url(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
]
```

templates/includes/pagination.html
```html
{% if is_paginated %}
  <nav aria-label="Topics pagination" class="mb-4">
    <ul class="pagination">
      {% if page_obj.has_previous %}
        <li class="page-item">
          <a class="page-link" href="?page={{ page_obj.previous_page_number }}">Previous</a>
        </li>
      {% else %}
        <li class="page-item disabled">
          <span class="page-link">Previous</span>
        </li>
      {% endif %}

      {% for page_num in paginator.page_range %}
        {% if page_obj.number == page_num %}
          <li class="page-item active">
            <span class="page-link">
              {{ page_num }}
              <span class="sr-only">(current)</span>
            </span>
          </li>
        {% else %}
          <li class="page-item">
            <a class="page-link" href="?page={{ page_num }}">{{ page_num }}</a>
          </li>
        {% endif %}
      {% endfor %}

      {% if page_obj.has_next %}
        <li class="page-item">
          <a class="page-link" href="?page={{ page_obj.next_page_number }}">Next</a>
        </li>
      {% else %}
        <li class="page-item disabled">
          <span class="page-link">Next</span>
        </li>
      {% endif %}
    </ul>
  </nav>
{% endif %}
```

templates/topic_post.html
```html
{% block content %}

  <div class="mb-4">
    <a href="{% url 'reply_topic' topic.board.pk topic.pk %}" class="btn btn-primary" role="button">Reply</a>
  </div>

  {% for post in posts %}
    <div class="card {% if forloop.last %}mb-4{% else %}mb-2{% endif %} {% if forloop.first %}border-dark{% endif %}">
      {% if forloop.first %}
        <div class="card-header text-white bg-dark py-2 px-3">{{ topic.subject }}</div>
      {% endif %}
      <div class="card-body p-3">
        <div class="row">
          <div class="col-2">
            <img src="{% static 'img/avatar.svg' %}" alt="{{ post.created_by.username }}" class="w-100">
            <small>Posts: {{ post.created_by.posts.count }}</small>
          </div>
          <div class="col-10">
            <div class="row mb-3">
              <div class="col-6">
                <strong class="text-muted">{{ post.created_by.username }}</strong>
              </div>
              <div class="col-6 text-right">
                <small class="text-muted">{{ post.created_at }}</small>
              </div>
            </div>
            {{ post.message }}
            {% if post.created_by == user %}
              <div class="mt-3">
                <a href="{% url 'edit_post' post.topic.board.pk post.topic.pk post.pk %}"
                   class="btn btn-primary btn-sm"
                   role="button">Edit</a>
              </div>
            {% endif %}
          </div>
        </div>
      </div>
    </div>
  {% endfor %}

  {% include 'includes/pagination.html' %}

{% endblock %}
```
templates/topics.html
```html
{% block content %}
  <div class="mb-4">
    <a href="{% url 'new_topic' board.pk %}" class="btn btn-primary">New topic</a>
  </div>

  <table class="table mb-4">
    <!-- table code suppressed -->
  </table>

  {% include 'includes/pagination.html' %}

{% endblock %}
```

## 我的账户视图

accounts/views.py
```python
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email', )
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user
```
urls.py
```
from django.conf.urls import url
from accounts import views as accounts_views

urlpatterns = [
    # ...
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
]

```

templates/my_account.html
```html
{% extends 'base.html' %}

{% block title %}My account{% endblock %}

{% block breadcrumb %}
  <li class="breadcrumb-item active">My account</li>
{% endblock %}

{% block content %}
  <div class="row">
    <div class="col-lg-6 col-md-8 col-sm-10">
      <form method="post" novalidate>
        {% csrf_token %}
        {% include 'includes/form.html' %}
        <button type="submit" class="btn btn-success">Save changes</button>
      </form>
    </div>
  </div>
{% endblock %}
```
base.html
```html
<a class="dropdown-item" href="{% url 'my_account' %}">My account</a>
```

## 支持markdown

* 首先，安装markdown: `pip install markdown`

修改boards/models.py
```python
from django.db import models
from django.utils.html import mark_safe
from markdown import markdown

class Post(models.Model):
    # ...

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))
```

把`topic_posts.html`里面的
```html
{{ post.message }}
```
改为
```html
{{ post.get_message_as_markdown }}
```

### markdown编辑器

## 人性化设置

修改最新回帖时间，显示为距离当前时间多久, 比如几分钟前、几小时前或几天前

首先，在settings.py里添加`django.contrib.humanize`变量
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',  # <- here

    'widget_tweaks',

    'accounts',
    'boards',
]
```

然后，修改templates/topics.html
```html
{% extends 'base.html' %}

{% load humanize %}

{% block content %}
  <!-- code suppressed -->

  <td>{{ topic.last_updated|naturaltime }}</td>

  <!-- code suppressed -->
{% endblock %}

## 头像

## 最后调整

### 按回帖时间排序

之前都是按照发帖时间对主题帖进行排序的，这样显然不太合理，我们应该按照发帖时间排序。

修改boards/views.py里的`reply_topic`函数
```python
@login_required
def reply_topic(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            topic.last_updated = timezone.now()  # <- here
            topic.save()                         # <- and here

            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'reply_topic.html', {'topic': topic, 'form': form})
```
和PostListView类里的`get_context_data`函数
```python
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'topic_posts.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):

        session_key = 'viewed_topic_{}'.format(self.topic.pk)  # <-- here
        if not self.request.session.get(session_key, False):
            self.topic.views += 1
            self.topic.save()
            self.request.session[session_key] = True           # <-- until here

        kwargs['topic'] = self.topic
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        self.topic = get_object_or_404(Topic, board__pk=self.kwargs.get('pk'), pk=self.kwargs.get('topic_pk'))
        queryset = self.topic.posts.order_by('created_at')
        return queryset
```

### 调整帖子

修改导航栏，加入页数显示和发帖者

首先，在models.py里面的Topic类添加一些函数：
```python
import math
from django.db import models

class Topic(models.Model):
    # ...

    def __str__(self):
        return self.subject

    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)
```

然后，在templates/topics.html里面部署
```html
<table class="table table-striped mb-4">
    <thead class="thead-inverse">
      <tr>
        <th>Topic</th>
        <th>Starter</th>
        <th>Replies</th>
        <th>Views</th>
        <th>Last Update</th>
      </tr>
    </thead>
    <tbody>
      {% for topic in topics %}
        {% url 'topic_posts' board.pk topic.pk as topic_url %}
        <tr>
          <td>
            <p class="mb-0">
              <a href="{{ topic_url }}">{{ topic.subject }}</a>
            </p>
            <small class="text-muted">
              Pages:
              {% for i in topic.get_page_range %}
                <a href="{{ topic_url }}?page={{ i }}">{{ i }}</a>
              {% endfor %}
              {% if topic.has_many_pages %}
              ... <a href="{{ topic_url }}?page={{ topic.get_page_count }}">Last Page</a>
              {% endif %}
            </small>
          </td>
          <td class="align-middle">{{ topic.starter.username }}</td>
          <td class="align-middle">{{ topic.replies }}</td>
          <td class="align-middle">{{ topic.views }}</td>
          <td class="align-middle">{{ topic.last_updated|naturaltime }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
```

### 优化回复页

回复页只显示最新的10条回复

boards/models.py
```python
class Topic(models.Model):
    # ...

    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]
```
templates/reply_topic.html
```python
{% block content %}

  <form method="post" class="mb-4" novalidate>
    {% csrf_token %}
    {% include 'includes/form.html' %}
    <button type="submit" class="btn btn-success">Post a reply</button>
  </form>

  {% for post in topic.get_last_ten_posts %}  <!-- here! -->
    <div class="card mb-2">
      <!-- code suppressed -->
    </div>
  {% endfor %}

{% endblock %}
```

### 优化回复后跳转

回复帖子后跳转到最后页

`templates/topic_posts.html`
```html
{% block content %}

  <div class="mb-4">
    <a href="{% url 'reply_topic' topic.board.pk topic.pk %}" class="btn btn-primary" role="button">Reply</a>
  </div>

  {% for post in posts %}
    <div id="{{ post.pk }}" class="card {% if forloop.last %}mb-4{% else %}mb-2{% endif %} {% if forloop.first %}border-dark{% endif %}">
      <!-- code suppressed -->
    </div>
  {% endfor %}

  {% include 'includes/pagination.html' %}

{% endblock %}
```

### 优化底部页数显示


# Part7 部署

[top](#学习Django)
