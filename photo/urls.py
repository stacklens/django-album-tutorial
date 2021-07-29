from django.urls import path
from photo.views import home, upload, oss_home

app_name = 'photo'

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
    path('oss-home/', oss_home, name='oss_home'),
]