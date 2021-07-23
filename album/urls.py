from django.contrib import admin
from django.urls import path, include
from photo.views import home


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('photo/', include('photo.urls', namespace='photo')),
    path('', home, name='home'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
