from django.urls import path
from photo.views import home

app_name = 'photo'

urlpatterns = [
    path('', home, name='home'),
]