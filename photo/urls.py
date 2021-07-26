from django.urls import path
from photo.views import home, upload

app_name = 'photo'

urlpatterns = [
    path('', home, name='home'),
    path('upload/', upload, name='upload'),
]