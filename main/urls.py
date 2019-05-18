
from django.contrib import admin
from django.urls import path, include
from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', include('booking.urls')),
    path('accounts/', include('authtools.urls')),
    path('accounts/', include('users.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
