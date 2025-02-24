from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),  # Include web application URLs
    path('api/', include('base.api.urls')),  # Include API URLs
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)