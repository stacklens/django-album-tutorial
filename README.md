[![](https://img.shields.io/badge/python-3.8.10-orange.svg)](https://www.python.org/downloads/release/python-370/)
[![](https://img.shields.io/badge/django-3.2.5-green.svg)](https://docs.djangoproject.com/en/2.1/releases/2.1/)
[![](https://img.shields.io/badge/bootstrap-5.0.2-blue.svg)](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[![](https://img.shields.io/badge/license-CC_BY_NC_4.0-000000.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# Django搭建网络相册教程

这是面向新人的**Django搭建网络相册教程**的项目代码。

**教程为零基础的小白准备，目的是快速搭建一个相册网站。**

教程传送门：

- [GitHub](/md)

> 文章位于 `/md` 目录中。

## 教程特点

- 零基础、免费、中文
- 基于 Python 3.8.10、Django 3.2.5 和 Bootstrap 5.0.2
- 完全开源的文章和代码

## 适合人群

- 拥有一台能开机的电脑
- 有一点基础的python编程知识
- 每天能抽出一个小时学习

不要犹豫，现在立刻开始Django的学习吧！

## 教程快照

**代码片段：**
![](/media/repo/readme-1.gif)

---

**博客首页片段：**
![](/media/repo/readme-2.gif)

---

**博客详情页片段：**
![](/media/repo/readme-3.gif)

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