Django 框架主要关注的是**模型**（Model）、**模板**（Template）和**视图**（Views），称为MTV模式。

它们各自的职责如下：

| 层次                     | 职责                                                         |
| ------------------------ | ------------------------------------------------------------ |
| 模型（Model），数据层    | 处理与数据相关的所有事务： 如何存取、如何验证有效性、数据之间的关系等。 |
| 模板（Template），表现层 | 处理与表现相关的事务，即数据如何在页面中进行显示。           |
| 视图（View），逻辑层     | 存取模型及调取恰当模板的相关逻辑。模型与模板的桥梁。         |

简单来说就是 Model 存取数据，View 决定需要调取哪些数据，而 Template 则负责将调取的数据以合理的方式展现出来。

本章主要聊聊模板，以及它们三者的交互。

## 小试牛刀

首先给 `Photo` 模型增加一个 `Meta` 内部类：

```python
# /photo/models.py

...

class Photo(models.Model):
    ...
    class Meta:
        ordering = ('-created',)
```

`ordering` 属性定义了图片数据的排序，比如这里是按创建时间倒序排列。

接着修改 `home()` 视图函数：

```python
# /photo/views.py

from django.shortcuts import render
from photo.models import Photo

def home(request):
    photos  = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo/list.html', context)
```

- 前面章节说过，Django 的 **ORM** 尽可能让你脱离晦涩的数据库操作语句。比如这里，模型类直接用 `Photo.objects.all()` 取出所有的图片模型对象，就和操作普通的 Python 对象差不多，相当亲切。
- 视图取出的数据最终要传递给模板，这些数据的集合被称为**上下文**（context），以字典的形式组织在一起。
- 将数据载入模板、填充上下文、返回响应体对象，这是常用的流程，因此 Django 提供了 `render()` 这个快捷函数。它的三个参数分别是当前请求体、模板所在路径和上下文字典。

接下来在项目根目录下新建 `/templates/photo/list.html` 模板文件：

```python
# /templates/photo/list.html

{% for photo in photos %}
  <img src="{{ photo.image.url }}" alt="">
{% endfor %}
```

- 模板里的逻辑语法以 `{% .. %}` 形式组织。Django 在渲染 html 文件时，碰到 `{% .. %}` 就知道这不是展现给用户的文字或符号，而是模板的控制流语句。
- 模板标签中的 `photos` 就是前面视图上下文中传递的 `photos` 数据。
- 模板里的数据用 `{{ ... }}` 组织，它是实实在在的需要动态替换成展现给用户的内容，注意它和控制流标签的区别。注意看，标签里的 `photo` 就是 `Photo` 模型的实例，`.image` 是模型里定义的图片字段，`.url` 是字段中包含的图片路径。
- 最后以 `{% endfor %}` 标志整个控制流的结束。

> `<img ...>` 这个就是普通的 `html` 标签了，教程虽然只会用到最基础的 html/css/javascript 知识，但篇幅有限不会展开讲解。如果阅读非常吃力建议先看一些相关基础。

模板虽然写好了，但是还没告诉 Django 模板文件的路径。默认的模板路径在每个 App 自己的路径中，但笔者习惯把所有模板文件集中在一起，因此需要改一下全局配置：

```python
# /album/settings.py

...
# 注意是修改此配置
# 不是新增
TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
        ...
    },
]
...
```

这就完工了。

运行服务器看看：（请确保已经在后台保存了一些图片数据）

![](https://blog.dusaiphoto.com/dj-album-50-1.jpg)

虽然没有任何样式，导致图片太大直接撑爆了屏幕，但整个 MTV 流程顺利打通了。

> 如果图片未正常显示，先打开浏览器的控制台看看有无 404 报错。有报错可能是前面章节有关媒体文件路径配置不正确（MEDIA_ROOT 等），无报错则可能是其他原因。

## 模板复用

模板文件实质上是 `html` 文件。 Django 会按照模板标签的规则，将里面的标签文本替换成对应的数据。

既然是普通的 html 文件，那么写的时候还是得按照其书写规范，不要乱来。

一个标准的 html 文档至少要包含下面的内容：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My test page</title>
  </head>
  <body>
    <p>This is my page</p>
  </body>
</html>
```

因此前面测试写的那个 `list.html` 得修改。

另一方面，html 文件与 Python 代码一样，很多地方是可以复用的。比如需要载入的资源啊、全局的基础样式啊、页眉页脚啊这些。因此模板也提供了办法来实现其复用，让我们实践看看。

### 基础模板

首先来写所有模板的“父类”，即全站的基础模板 `/templates/base.html` ：

```html
<!-- /templates/base.html -->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <!-- 预留页面标题位置 -->
    <title>{% block title %}{% endblock title %}</title>
    <!-- bootstrap.css -->
    <link
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" 
    rel="stylesheet" 
    integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" 
    crossorigin="anonymous">
  </head>
  <body>
    <!-- 引入导航栏 -->
    {% include 'header.html' %}
    <!-- 预留具体页面的位置 -->
    {% block content %}{% endblock content %}
    <!-- 引入注脚 -->
    {% include 'footer.html' %}
    <!-- bootstrap.js -->
    <script 
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" 
    integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
    crossorigin="anonymous"></script>
    <script 
    src="https://cdn.jsdelivr.net/npm/masonry-layout@4.2.2/dist/masonry.pkgd.min.js" 
    integrity="sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D"
    crossorigin="anonymous" 
    async></script>
    <!-- 预留脚本的位置 -->
    {% block scripts %}{% endblock scripts %}
      
    <style>
        body {
            background-color:#212529;
        }
    </style>
  </body>
</html>
```

有点长但不复杂，来分解一下：

- 它是个规范的 html 文档。
- `{% block ... %}` 给“继承”它的“模板子类”预留出空间，表示这个位置的内容将由“子类”来填充。
- `{% include '...' %}` 表示在这个位置，插入另外一个模板文件。也就是页眉和页脚了。
- 它远程引用了 `Bootstrap` 的 css/js 文件。 [Bootstrap](https://getbootstrap.com/) 是非常流行的前端响应式框架，上手极其简单（直接在官网抄示例代码），用它可以非常高效写出屏幕自适应的现代化页面。
- 引入了后续卡片效果要用的瀑布流插件 `masonry.js` 。
- 将全局背景设置为深灰色。

### 页眉和页脚

理论上页眉和页脚也是全站点共用的，也可以直接写在 `base.html` 里。不过为了保持干净，还是独立出来好了。

首先是新建**页眉**模板文件：

```html
<!-- /templates/header.html -->

<!-- 导航栏 -->
<nav class="navbar navbar-dark bg-dark">
    <div class="container">
        <!-- 标志 -->
        <a class="navbar-brand" href="#">
            <h2>Awesome Album</h2>
        </a>
    </div>
</nav>
```

非常简单，就是一个普通的 Bootstrap 导航栏标签。

注意此文件的路径，和 `base.html` 里的 `{% include 'header.html' %}` 要能够对应。

接着是**页脚**：

```html
<!-- /templates/footer.html -->

<!-- Footer -->
<div><br><br><br></div>
<footer class="py-3 bg-dark fixed-bottom">
    <div class="container">
        <p class="m-0 text-center text-white">
            Copyright &copy; www.dusaiphoto.com 2021
        </p>
    </div>
</footer>
```

也很简单，是一个固定在底部的横幅。

### 图片列表

最后才是正儿八经的图片列表模板。

修改 `list.html` 文件如下：

```html
<!-- /templates/photo/list.html -->

{% extends "base.html" %}
{% block title %}首页{% endblock title %}

{% block content %}
    {% for photo in photos %}
        <img src="{{ photo.image.url }}" alt="">
    {% endfor %}
{% endblock content %}

```

- `{% extends "base.html" %}` 表示此模板“继承”自 `base.html` 。
- 注意看 `{% block title %}` 等标签和 `base.html` 的对应关系。

重启服务器看看效果：

![](https://blog.dusaiphoto.com/dj-album-50-2.jpg)

绕了一圈，除了页眉页脚，看上去似乎没啥变化，但是模板文件的结构变清晰了。

## 模板布局

上面这种撑爆屏幕的图片效果肯定是没法用的。

我们按照 Bootstrap 官方给的[卡片示例代码](https://getbootstrap.com/docs/5.0/components/card/)稍微改一下：

```html
<!-- /templates/photo/list.html -->

{% extends "base.html" %}
{% block title %}首页{% endblock title %}

{% block content %}
    <div class="container py-2">
        <div class="row" data-masonry='{"percentPosition": true}'>
            {% for photo in photos %}
            <div class="col-4 py-2">
                <div class="card">
                    <img 
                    src="{{ photo.image.url }}" 
                    alt=""
                    class="card-img"
                    >
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
{% endblock content %}
```

在后台中再多添加一些图片数据。

> 教程示例均来自[pixabay](https://pixabay.com/zh/illustrations/)免费商用图片，此致感谢。

刷新页面看看效果：

![](https://blog.dusaiphoto.com/dj-album-50-3.jpg)

Bootstrap 把复杂的布局技术隐藏起来，你只需要引入它并按照它的规则修改 `class` 等属性就可以获得非常漂亮、屏幕自适应的界面。

## 总结

目前为止，我们只写了非常少的 Python 代码（不到三十行），和非常简单的 html 代码，就获得了像模像样的相册网站了，说不定可以拿去交付（忽悠）甲方了。 Django 和 Bootstrap 的配合还不错吧？

下一章将通过照片细节展示功能，探讨模态与动画技术。

> 点赞和吐槽？评论区来告诉我！
