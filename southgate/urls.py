from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('pages/', include('pages.urls')),
    path('securelogin/', admin.site.urls),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
