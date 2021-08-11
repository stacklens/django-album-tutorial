from django.urls import path
from photo.views import (
        home,
        upload,
        oss_home, 
        fetch_photos,
    )

from django.views.generic import TemplateView

app_name = 'photo'

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('oss-home/', oss_home, name='oss_home'),
    path(
        'endless-home/',
        TemplateView.as_view(template_name='photo/endless_list.html'),
        name='endless_home'
    ),
    path('fetch/', fetch_photos, name='fetch'),
]