学习Django
====

[![Python Version](https://img.shields.io/badge/python-3.6.5-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-1.11.4-brightgreen.svg)](https://djangoproject.com)

最近在学习Python，看小甲鱼的视频，并参考了[TwoWater](https://github.com/TwoWater)的[草根学Python](https://github.com/TwoWater/Python), 其中提到了Django，和国外一个博客上的Django教程。遂开始学习Django.

## Django教程

一个浅显易懂的Django教程: [A Complete Beginner's Guide to Django](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/)

该教程共包含7个部分（Part）,以搭建一个论坛为例子，较为详细地介绍了Django搭建流程。

在Github上有关于它的中文翻译: [A Complete Beginner's Guide to Django 翻译计划](https://github.com/wzhbingo/django-beginners-guide), 不过只有前2个Part是完整翻译的，剩下的没翻译完，好像是中止了，所以后面的部分我都是看的英文原版)。

根据教程一步一步执行命令，遇到问题并解决问题，虽然大多数问题是漏了某个步骤或某行代码，但在解决问题的过程中会仔细查看代码和步骤，这样就加深了理解。而且，由于其中涉及了不少HTML, CSS等相关
知识，需要的时候也去看看，学到不少。

为防止遗忘，自己动手做一个简略版的记录，也方便以后需要的时候回看。 

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
    - [可重用Templates](#可重用templates)
    - [表单](#表单)
- [Part4 身份验证](#part4-身份验证)
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

## Hello, World!

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

## 可重用Templates

## 表单

# Part4 身份验证

[top](#学习Django)

# Part5 Django ORM

[top](#学习Django)

# Part6 基于类的视图

[top](#学习Django)

# Part7 部署

[top](#学习Django)
