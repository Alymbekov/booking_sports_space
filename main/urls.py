
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import  settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('booking.urls', namespace="booking")),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls', namespace='user')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)









