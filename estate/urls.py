from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from estate import settings

urlpatterns = [
    path('admindeveloper/', admin.site.urls),
    path('', include('properties.urls')),
    path('accounts/', include('allauth.urls')),
    
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

