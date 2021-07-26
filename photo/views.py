from django.shortcuts import render, redirect
from photo.models import Photo
from django.contrib.auth import authenticate, login, logout

def home(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    # 处理登入登出的POST请求
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user     = authenticate(request, username=username, password=password)
        # 登入
        if user is not None and user.is_superuser:
            login(request, user)
        # 登出
        isLogout  = request.POST.get('isLogout')
        if isLogout == 'True':
            logout(request)
    return render(request, 'photo/list.html', context)


def upload(request):
    if request.method == 'POST' and request.user.is_superuser:
        images = request.FILES.getlist('images')
        for i in images:
            photo = Photo(image=i)
            photo.save()
    return redirect('home')