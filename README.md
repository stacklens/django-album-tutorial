[![](https://img.shields.io/badge/python-3.8.10-orange.svg)](https://www.python.org/downloads/release/python-370/)
[![](https://img.shields.io/badge/django-3.2.5-green.svg)](https://docs.djangoproject.com/en/2.1/releases/2.1/)
[![](https://img.shields.io/badge/bootstrap-5.0.2-blue.svg)](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[![](https://img.shields.io/badge/license-CC_BY_NC_4.0-000000.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# Django搭建网络相册教程

这是面向新人的**Django搭建网络相册教程**。

**教程为零基础的小白准备，目的是快速搭建一个相册网站。**

教程传送门：

- [GitHub](/md)

> 文章位于 `/md` 目录中。

## 什么是 Django

**Django** 是一个由 **Python** 写成的开源Web应用框架，你可以用它以更高的效率、更少的代码，轻松搭建一个高性能的网站。

如果你以前从未接触过 web 开发，并且想快速上线自己的个性化网站，Django 是你的绝佳选择。

在本教程中，你会见识到 Django 如何用非常少量、简单易懂的代码，完成功能强大的网站。

## 教程特点

- 零基础、免费、中文
- 基于 Python 3.8.10、Django 3.2.5 和 Bootstrap 5.0.2
- 完全开源的文章和代码

## 适合人群

- 拥有一台能开机的电脑
- 具有基础的python编程知识
- 每天能抽出一个小时学习

**后端知识**具有 `Python` 和 `Django` 基础就足够了。

如果本教程你看着非常吃力，那么可以先看看我的 Django 博客入门教程：

- [博客传送门](https://www.dusaiphoto.com/article/2/)
- [GitHub传送门](https://github.com/stacklens/django_blog_tutorial/tree/master/md)

> 微信公众号也同步更新，搜“杜赛说编程”即可。

**前端知识**具有 `html/css/javascript` 基础即可，教程中不会涉及高深的前端知识。

不要犹豫，现在立刻开始Django的学习吧！

## 教程快照

![](/media/repo/readme-1.gif)

![](/media/repo/readme-2.gif)

![](/media/repo/readme-3.gif)

## 知识点

你将在本教程中学到的知识：

- 搭建开发环境
- Django 代码结构
- 数据存储
- MTV 模式
- 模态与动画
- 登入与登出
- 批量上传图片
- 分页
- 云存储
- 部署

共十个章节，都是浓缩的知识点，勤奋的你只需要奋斗十个晚上就足够看完了。

## 资源列表

本教程的代码托管在 GitHub：[Django-album-tutorial](https://github.com/stacklens/django-album-tutorial)

Django 的官方网站：[Django](https://www.djangoproject.com/)

项目开发完毕后使用 Git/GitHub 分布式管理：[Windows环境下使用Git和GitHub](https://www.dusaiphoto.com/article/article-detail/13/)

## 遇到困难时怎么办

- 认真检查代码拼写、缩进是否正确。一个标点符号的错误可能会导致难以发现的问题
- 较简单的问题直接询问百度；若无法得到满意的答案请尝试 Google 以英文关键字搜索。要坚信全世界这么多学习 Django 的人，你遇到的问题别人早就遇到过了
- [Django官方网站](https://www.djangoproject.com/)是最权威的学习文档，英语不佳的同学，要有耐心仔细阅读
- 在本教程下留言，博主会尽量帮忙解决；也可以私信我：dusaiphoto@foxmail.com
- 实在无法处理的问题，可以暂时跳过。待到技术水平上升台阶，再回头来解决问题
- 若以上办法均不能解决你的问题，请在[StackOverflow](https://stackoverflow.com/)等技术网站上求助，那里有海量的热心程序员在等着你的问题

## 关于版本

本教程基于 Python 3.8.10、Django 3.2.5 和 Bootstrap 5.0.2。推荐读者采用完全一致的版本，以避免不必要的兼容问题。于 Win 10 系统开发。用 Mac 或 Linux 也 OK。

> 特别要注意的是，教程后期关于对象存储的章节，相关的库目前为止（2021.07.29）仅支持到 Python 3.8 。使用 Python 3.9 可能会有潜在的 bug。

## 代码使用说明

确认你的电脑已经正确安装 Python。

下载项目后，在命令行中进入项目目录，并创建**虚拟环境**：

```bash
python -m venv env
```

运行**虚拟环境**（Windows环境）:

```bash
env\Scripts\activate.bat
```

或（Linux环境）：

```bash
source env/bin/activate
```

自动安装所有依赖项：

```bash
pip install -r requirements.txt
```

然后进行数据迁移：

```bash
python manage.py migrate
```

最后运行测试服务器：

```bash
python manage.py runserver
```

项目就运行起来了。

管理员账号：`dusai`  密码：`admin123456`

如果你想清除所有数据及媒体文件，将它们直接删除，并运行：

```bash
python manage.py createsuperuser
```

即可重新创建管理员账号。

## 开始你的表演

说了这么多，相信你已经迫不及待了。让我们赶紧开始旅程吧！

## 社区

**一个人的学习是孤单的。欢迎扫码 Django 交流QQ群（107143175）、博主公众号、TG群组，和大家一起进步吧！**

![](https://blog.dusaiphoto.com/QR-0608.jpg)

## 许可协议

本教程（包括且不限于文章、代码、图片等内容）遵守 **署名-非商业性使用 4.0 国际 (CC BY-NC 4.0) 协议**。协议内容如下。

**您可以自由地：**

- **共享** — 在任何媒介以任何形式复制、发行本作品。
- **演绎** — 修改、转换或以本作品为基础进行创作。

只要你遵守许可协议条款，许可人就无法收回你的这些权利。

**惟须遵守下列条件：**

- **署名** — 您必须给出**适当的署名**，提供指向本许可协议的链接，同时标明是否（对原始作品）作了修改。您可以用任何合理的方式来署名，但是不得以任何方式暗示许可人为您或您的使用背书。
- **非商业性使用** — 您不得将本作品用于**商业目的**。

- **没有附加限制** — 您不得适用法律术语或者技术措施从而限制其他人做许可协议允许的事情。

> 适当的署名：您必须提供创作者和署名者的姓名或名称、版权标识、许可协议标识、免责标识和作品链接。
>
> 商业目的：主要目的为获得商业优势或金钱回报。