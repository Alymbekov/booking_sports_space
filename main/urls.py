
from django.contrib import admin

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('booking.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









