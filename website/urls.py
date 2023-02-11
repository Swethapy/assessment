from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin/
    path('admin/', admin.site.urls),
    
    # core/
    path('core/', include('core.urls', namespace='core')),
    
    # api/
    path('api/', include('api.urls', namespace='api')),
]
