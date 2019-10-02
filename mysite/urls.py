
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import  static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('courses.urls', namespace='courses')),
]

# adding urls for the media files to be accessed 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)